from django.urls import path

from . import views

urlpatterns = [
    path('', views.obtain_latest_data, name='obtain_latest_data'),
]
