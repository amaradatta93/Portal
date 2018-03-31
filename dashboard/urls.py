from django.urls import path
from django.views.generic import TemplateView

from . import views, utils

app_name = 'dashboard'

urlpatterns = [
    path('', views.obtain_latest_data, name='obtain_latest_data'),
    path('add/', TemplateView.as_view(template_name='add_stock.html'), name='add_stock'),
]
