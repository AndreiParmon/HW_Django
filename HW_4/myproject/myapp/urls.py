from django.urls import path
from .views import *

urlpatterns = [
    path('last_week/', last_week, name='last_week'),
    path('last_month/', last_month, name='last_month'),
    path('last_year/', last_year, name='last_year'),
    path('product/add/', product_form, name='product_form'),
]
