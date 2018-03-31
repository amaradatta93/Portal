from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dashboard.utils import get_all, raw_data


@login_required
def obtain_latest_data(request):
    stocks = get_all(request.user)
    parsed_data = []
    for stock in stocks:
        tckr = stock.company_ticker_name
        json_data = raw_data(tckr)
        meta_data = {}
        date = json_data['Meta Data']['3. Last Refreshed']
        price_data = json_data['Time Series (60min)'][date]
        meta_data['price'] = {}
        meta_data['price']['open'] = price_data['1. open']
        meta_data['date'] = date
        meta_data['ticker'] = tckr
        parsed_data.append(meta_data)
    return render(request, 'dashboard.html', {'parsed_data': parsed_data})
