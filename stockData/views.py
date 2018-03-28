import os
from urllib.parse import urlencode

import requests
from django.http import JsonResponse

API_KEY = os.getenv('API_KEY')


def access_stock_data(ticker):
    params = urlencode(dict(function='TIME_SERIES_INTRADAY',
                            symbol=ticker,
                            interval='60min',
                            outputsize='compact',
                            apikey=API_KEY))
    url = 'https://www.alphavantage.co/query?{0}'.format(params)
    return url


def raw_data(ticker):
    url = access_stock_data(ticker)
    json_stock_data = requests.get(url).json()
    return json_stock_data


def obtain_latest_data(request):
    company_ticker = get_all()
    parsed_data = {}
    for tckr in company_ticker:
        json_data = raw_data(tckr)
        date = json_data['Meta Data']['3. Last Refreshed']
        parsed_data[tckr] = {'Meta Data': json_data['Meta Data'], 'Current Price': json_data['Time Series (60min)'][date]}
    return JsonResponse(parsed_data)


def add_user_ticker(request):
    pass
    # if request.method == 'POST':
    #     stockData = StockData()
    #     stockData.company_name = ''
    #     stockData.company_ticker_name= ''
    #     stockData.save()


def delete__user_ticker():
    pass


def get_all():
    # stocks = get_object_or_404(StockData)
    # return HttpResponse(list(stocks.company_ticker_name))
    return ['MSFT', 'FB', 'AAPL', 'GOOGL', 'NFLX']
