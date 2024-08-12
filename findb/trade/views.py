from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Holding, Security, Transaction
from .forms import TradeForm
import yfinance as yf
from decimal import Decimal

def get_current_price(symbol):
    return Decimal((yf.Ticker(symbol)).info['currentPrice'])  # This function will fetch the latest price

@login_required
def trade_view(request):
    user = request.user
    portfolio, created = Portfolio.objects.get_or_create(user=user)
    form = TradeForm()

    if request.method == 'POST':
        if 'confirm_trade' in request.POST:
            # Execute the trade
            ticker = request.POST.get('ticker')
            quantity = Decimal(request.POST.get('quantity'))
            action = request.POST.get('action')
            price = get_current_price(ticker)
            total_cost = quantity * price

            if action == 'buy':
                if portfolio.balance >= total_cost:
                    portfolio.balance -= total_cost
                    portfolio.save()

                    holding, created = Holding.objects.get_or_create(portfolio=portfolio, security__symbol=ticker)
                    holding.quantity += quantity
                    holding.save()

                else:
                    return render(request, 'trade/trade.html', {
                        'form': form,
                        'error': 'Insufficient balance',
                        'portfolio_balance': portfolio.balance,
                        'holdings': portfolio.holdings.all(),
                        'transactions': portfolio.transaction_set.all(),
                    })
            elif action == 'sell':
                try:
                    holding = Holding.objects.get(portfolio=portfolio, security__symbol=ticker)
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
                            'error': 'Not enough holdings to sell',
                            'portfolio_balance': portfolio.balance,
                            'holdings': portfolio.holdings.all(),
                            'transactions': portfolio.transaction_set.all(),
                        })
                except Holding.DoesNotExist:
                    return render(request, 'trade/trade.html', {
                        'form': form,
                        'error': 'You do not own any of this security',
                        'portfolio_balance': portfolio.balance,
                        'holdings': portfolio.holdings.all(),
                        'transactions': portfolio.transaction_set.all(),
                    })

            Transaction.objects.create(
                portfolio=portfolio,
                security=Security.objects.get(symbol=ticker),
                quantity=quantity if action == 'buy' else -quantity,
                price_at_transaction=price
            )

            return render(request, 'trade/trade.html', {
                'form': form,
                'success': True,
                'ticker': ticker,
                'quantity': quantity,
                'price': price,
                'total_cost': total_cost,
                'remaining_balance': portfolio.balance,
                'action': action,
                'portfolio_balance': portfolio.balance,
                'holdings': portfolio.holdings.all(),
                'transactions': portfolio.transaction_set.all(),
            })
        else:
            form = TradeForm(request.POST)
            if form.is_valid():
                ticker = form.cleaned_data['ticker'].upper()
                quantity = form.cleaned_data['quantity']
                action = form.cleaned_data['action']
                price = get_current_price(ticker)
                total_cost = Decimal(quantity) * price

                return render(request, 'trade/trade.html', {
                    'form': form,
                    'confirm': True,
                    'ticker': ticker,
                    'quantity': quantity,
                    'price': price,
                    'total_cost': total_cost,
                    'remaining_balance': portfolio.balance - total_cost if action == 'buy' else portfolio.balance + total_cost,
                    'action': action,
                    'portfolio_balance': portfolio.balance,
                    'holdings': portfolio.holdings.all(),
                    'transactions': portfolio.transaction_set.all(),
                })

    return render(request, 'trade/trade.html', {
        'form': form,
        'portfolio_balance': portfolio.balance,
        'holdings': portfolio.holdings.all(),
        'transactions': portfolio.transaction_set.all(),
    })