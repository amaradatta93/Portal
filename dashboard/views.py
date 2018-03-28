from django.http import HttpResponse

from stockData.models import StockData


def user_stock(request):
    return HttpResponse("Hello, world. You will get the stock data.")
