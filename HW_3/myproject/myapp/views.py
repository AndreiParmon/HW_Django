from django.shortcuts import render
import logging
from myapp.models import Client, Product, Order
from datetime import datetime, timedelta


def dateValue(first: str, second: str) -> bool:
    f_year = int(first[0] + first[1] + first[2] + first[3])
    s_year = int(second[0] + second[1] + second[2] + second[3])

    f_month = int(first[5] + first[6])
    s_month = int(second[5] + second[6])

    f_day = int(first[8] + first[9])
    s_day = int(second[8] + second[9])

    f_res = f_year * 365 + f_month * 30 + f_day
    s_res = s_year * 365 + s_month * 30 + s_day

    if f_res >= s_res:
        return True
    else:
        return False


def last_week(request):
    date = datetime.today() - timedelta(days=7)
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'
    context['orders'] = orders
    return render(request, "myapp/index.html", context)


def last_month(request):
    date = datetime.today() - timedelta(days=30)
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'

    context['orders'] = orders
    return render(request, "myapp/index.html", context)


def last_year(request):
    date = datetime.today() - timedelta(days=365)
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'

    context['orders'] = orders
    return render(request, "myapp/index.html", context)
