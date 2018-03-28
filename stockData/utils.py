import os
from urllib.parse import urlencode

import requests

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


def get_all():
    # stocks = get_object_or_404(StockData)
    # return HttpResponse(list(stocks.company_ticker_name))
    return ['MSFT', 'FB', 'AAPL', 'GOOGL', 'NFLX']
