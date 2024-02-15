from django.shortcuts import render, redirect

# Create your views here.
import json
from django.core.paginator import Paginator
from .models import Stock


def home_page(request):

    data = Stock.objects.all().order_by("date")

    paginator = Paginator(data, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj})


def single_stock(request, sid):
    data = Stock.objects.get(pk=sid)
    return render(request, "single_stock.html", {"item": data})


def update_stock(request, sid):
    for key, value in request.POST.items():
        print(key, value)
    if request.method == "POST":
        date = request.POST.get("date")
        trade_code = request.POST.get("trade_code")
        high = request.POST.get("high")
        low = request.POST.get("low")
        open = request.POST.get("open")
        close = request.POST.get("close")
        volume = request.POST.get("volume")

        item = Stock.objects.get(pk=sid)
        item.date = date
        item.trade_code = trade_code
        item.high = high
        item.low = low
        item.open = open
        item.close = close
        item.volume = volume
        item.save()
        return redirect("home")

    data = Stock.objects.get(pk=sid)
    return render(request, "update_stock.html", {"item": data})


def delete_stock(request, sid):
    data = Stock.objects.get(pk=sid)
    data.delete()
    return redirect("home")
