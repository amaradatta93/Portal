from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect

from .forms import StockForm, DeleteForm
from .models import StockData


@login_required
def add_user_ticker(request):
    if request.method == 'POST':
        stock_form = StockForm(request.POST)

        if stock_form.is_valid():
            stockdata = StockData()
            stockdata.stockholder = request.user
            stockdata.company_name = stock_form.cleaned_data['name']
            stockdata.company_ticker_name = stock_form.cleaned_data['ticker_name']

            try:
                stockdata.save()
                messages.success(request, 'Saved the stock')
            except IntegrityError:
                messages.warning(request, 'You already saved this stock.')

            return redirect('/')

        else:
            messages.error(request, 'Enter a valid input')
            return redirect('/')


@login_required
def delete_user_ticker(request):
    if request.method == 'POST':
        stock_form = DeleteForm(request.POST)

        if stock_form.is_valid():
            ticker_name = stock_form.cleaned_data['ticker_name']
            stockdata = StockData.objects.filter(company_ticker_name=ticker_name)

            if stockdata:
                stockdata.delete()
                messages.success(request, 'Successfully deleted the stock')
            else:
                messages.warning(request, 'No such stocks exist')

        else:
            messages.error(request, 'Please enter a valid ticker')
        return redirect('/')
