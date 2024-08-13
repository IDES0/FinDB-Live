from django.db import models
from django.contrib.auth.models import User
import yfinance as yf # Change this later

# Represents securities that are available to trade
class Security(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol

# Represents user porfolio (balance and related holdings)
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=10000.00)  # Default starting balance

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

# Represents quantity of each security a user holds
class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='holdings')
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Supports fractional shares

    def __str__(self):
        return f"{self.quantity} of {self.security.symbol} in {self.portfolio}"

# Records each buy/sell action from the user, captures quantity and price at time of trade
class Transaction(models.Model): 
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    price_at_transaction = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.security.symbol} at {self.price_at_transaction}"