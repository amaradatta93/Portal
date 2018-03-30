from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import StockForm
from .models import StockData


@login_required
def add_user_ticker(request):
    saved = False
    stockdata = {}

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
            print(stockdata.company_name, stockdata.company_ticker_name)
            # return render(request, 'saved.html', {'saved': saved})
            return HttpResponse(stockdata.company_name)
        else:
            return HttpResponse('hi')
        # return JsonResponse({'name':stockdata.company_name, 'tckr': stockdata.company_ticker_name})


def delete_user_ticker(request):
    pass
