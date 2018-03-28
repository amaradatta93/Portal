from django.db import models


class Stockholder(models.Model):
    stock_holder_first_name = models.CharField(max_length=100)
    stock_holder_last_name = models.CharField(max_length=100)
    stock_holder_email = models.EmailField()
    stock_holder_password = models.CharField(max_length=30)

    def as_dict(self):
        return {
            'first_name': self.stock_holder_first_name,
            'last_name ': self.stock_holder_last_name,
            'email': self.stock_holder_email,
            'id': self.pk
        }