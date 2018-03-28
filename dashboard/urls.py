from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_stock, name='user_stock'),
]
