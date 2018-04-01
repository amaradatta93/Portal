from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import StockForm
from .models import StockData


@login_required
def add_user_ticker(request):
    if request.method == 'POST':
        saved = False
        stock_form = StockForm(request.POST)

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


@login_required
def delete_user_ticker(request):
    if request.method == 'POST':
        stock_form = StockForm(request.POST)

        if stock_form.is_valid():
            ticker_name = stock_form.cleaned_data['ticker_name']
            stockdata = StockData.objects.filter(company_ticker_name=ticker_name)
            stockdata.delete()
            deleted = True
            return render(request, 'deleted.html', {'deleted': deleted})
