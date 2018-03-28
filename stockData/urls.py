from django.urls import path

from . import views

urlpatterns = [
    path('', views.raw_data, name='raw_data'),
]
