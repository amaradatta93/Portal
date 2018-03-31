import os
from urllib.parse import urlencode

import requests

from stockData.models import StockData

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


def get_all(stockholder):
    stocks = StockData.objects.filter(stockholder=stockholder)
    return stocks
