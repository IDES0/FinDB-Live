from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Holding, Security, Transaction
from .forms import TradeForm
import yfinance as yf
from decimal import Decimal

def get_current_price(symbol):
    return Decimal((yf.Ticker(symbol)).info['currentPrice'])  # Fetches the latest price

@login_required
@login_required
def trade_view(request):
    user = request.user
    portfolio, created = Portfolio.objects.get_or_create(user=user)
    form = TradeForm()

    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker'].upper()
            quantity = form.cleaned_data['quantity']
            action = form.cleaned_data['action']
            
            # Get or create the security object using the correct field
            security, created = Security.objects.get_or_create(symbol=ticker)
            
            # Fetch the latest price
            price = get_current_price(ticker)
            total_cost = Decimal(quantity) * Decimal(price)

            if action == 'buy':
                # Ensure sufficient funds
                if portfolio.balance >= total_cost:
                    portfolio.balance -= total_cost
                    portfolio.save()

                    # Add or update the holding
                    holding, created = Holding.objects.get_or_create(portfolio=portfolio, security=security)
                    holding.quantity += quantity
                    holding.save()
                else:
                    return render(request, 'trade/trade.html', {
                        'form': form,
                        'error': 'Insufficient balance'
                    })
            elif action == 'sell':
                try:
                    holding = Holding.objects.get(portfolio=portfolio, security=security)
                    if holding.quantity >= quantity:
                        holding.quantity -= quantity
                        portfolio.balance += total_cost
                        portfolio.save()
                        if holding.quantity == 0:
                            holding.delete()
                        else:
                            holding.save()
                    else:
                        return render(request, 'trade/trade.html', {
                            'form': form,
                            'error': 'Not enough holdings to sell'
                        })
                except Holding.DoesNotExist:
                    return render(request, 'trade/trade.html', {
                        'form': form,
                        'error': 'You do not own any of this security'
                    })

            # Render a summary of the trade
            return render(request, 'trade/trade.html', {
                'form': form,
                'ticker': ticker,
                'quantity': quantity,
                'price': price,
                'total_cost': total_cost,
                'remaining_balance': portfolio.balance,
                'action': action,
                'success': True,  # This flag can be used in your template to show the trade was successful
            })
    return render(request, 'trade/trade.html', {'form': form})

@login_required
def portfolio_view(request):
    portfolio = Portfolio.objects.get(user=request.user)
    holdings = portfolio.holdings.all()
    return render(request, 'trade/portfolio.html', {'portfolio': portfolio, 'holdings': holdings})