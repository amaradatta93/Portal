from django.db import models


class Stockholder(models.Model):
    stock_holder_first_name = models.CharField(max_length=100)
    stock_holder_last_name = models.CharField(max_length=100)
    stock_holder_email = models.EmailField()
    stock_holder_password = models.CharField(max_length=30)


