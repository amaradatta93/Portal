from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import StockForm
from .models import StockData


@login_required
def add_user_ticker(request):

    if request.method == 'POST':
        stock_form = StockForm(request.POST)
        print(stock_form.errors)
        print('entering')
        print(stock_form.cleaned_data['name'])

        if stock_form.is_valid():
            stockdata = StockData()
            stockdata.stockholder = request.user
            stockdata.company_name = stock_form.cleaned_data['name']
            stockdata.company_ticker_name = stock_form.cleaned_data['ticker_name']
            stockdata.save()
            saved = True
            return render(request, 'saved.html', {'saved': saved})
        else:
            return messages.error(request, "Error")


def delete_user_ticker(request):
    pass
