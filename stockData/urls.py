from django.urls import path

from . import views


app_name = 'stocks'


urlpatterns = [
    path('add/', views.add_user_ticker, name='add_user_ticker'),
    path('delete/', views.delete_user_ticker, name='delete_user_ticker'),
]
