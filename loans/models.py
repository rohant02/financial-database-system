from django.db import models
from users.models import CustomUser

class Loan(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
