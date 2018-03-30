from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dashboard.utils import get_all, raw_data


@login_required
def obtain_latest_data(request):
    company_ticker = get_all()
    parsed_data = {}
    for tckr in company_ticker:
        json_data = raw_data(tckr)
        date = json_data['Meta Data']['3. Last Refreshed']
        parsed_data[tckr] = {'Meta Data': json_data['Meta Data'],
                             'Current Value': json_data['Time Series (60min)'][date]}
    return render(request, 'dashboard.html', parsed_data)
