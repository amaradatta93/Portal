from django.contrib.auth.models import User
from django.db import models


class StockData(models.Model):
    stockholder = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_ticker_name = models.CharField(max_length=10)

    def as_dict(self):
        return {
            'id': self.pk,
            'stockholder_id': self.stockholder.pk,
            'company_name': self.company_name,
            'company_ticker_name': self.company_ticker_name
        }
