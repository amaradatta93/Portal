from django.urls import path

from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.obtain_latest_data, name='obtain_latest_data'),
]
