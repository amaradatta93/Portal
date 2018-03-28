from django.contrib.auth.models import User
from django.db import models


class StockData(models.Model):
    stockholder = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_percentage_change = models.CharField(max_length=10)
    company_trade_price = models.CharField(max_length=50)
