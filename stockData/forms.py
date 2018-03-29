from django import forms


class StockForm(forms.Form):
    name = forms.CharField()
    ticker_name = forms.CharField()
