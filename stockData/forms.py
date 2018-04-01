from django import forms
from django.contrib.auth.decorators import login_required


@login_required
class StockForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)
    ticker_name = forms.CharField(label='ticker_name', max_length=10)
