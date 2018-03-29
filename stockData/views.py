from django.shortcuts import render

from .forms import StockForm
from .models import StockData


def add_user_ticker(request):
    saved = False
    stockdata = None
    if request.method == 'POST':
        stock_form = StockForm(request.POST, request.FILES)

        if stock_form.is_valid():
            stockdata = StockData()
            stockdata.company_name = stock_form.cleaned_data["name"]
            stockdata.company_ticker_name = stock_form.cleaned_data["ticker_name"]
            stockdata.save()
            saved = True
    return render(request, 'saved.html', {'saved': saved, 'id': stockdata.company_name + ' data'})


def delete_user_ticker(request):
    pass
