from django.db import models

from users.models import Stockholder


class StockData(models.Model):
    stockholder = models.ForeignKey(Stockholder, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_percentage_change = models.CharField(max_length=10)
    company_trade_price = models.CharField(max_length=50)
