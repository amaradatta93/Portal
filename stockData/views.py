from django.http import JsonResponse

from stockData.utils import get_all, raw_data


def obtain_latest_data(request):
    company_ticker = get_all()
    parsed_data = {}
    for tckr in company_ticker:
        json_data = raw_data(tckr)
        date = json_data['Meta Data']['3. Last Refreshed']
        parsed_data[tckr] = {'Meta Data': json_data['Meta Data'],
                             'Current Price': json_data['Time Series (60min)'][date]}
    return JsonResponse(parsed_data)


def add_user_ticker(request):
    pass
    # if request.method == 'POST':
    #     stockData = StockData()
    #     stockData.company_name = ''
    #     stockData.company_ticker_name= ''
    #     stockData.save()


def delete__user_ticker(request):
    pass
