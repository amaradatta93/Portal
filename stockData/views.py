from django.http import HttpResponse


def raw_data(request):
    return HttpResponse("Hello, world. You will get the stock data.")
