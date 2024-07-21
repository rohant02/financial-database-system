from django.db import models
from accounts.models import Account

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')])
    date = models.DateTimeField(auto_now_add=True)
