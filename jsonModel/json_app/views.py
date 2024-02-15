from django.shortcuts import render

# Create your views here.
import json
from django.core.paginator import Paginator


def home_page(request):
    with open("stock_market_data.json") as f:
        data = json.load(f)

    paginator = Paginator(data, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj})
