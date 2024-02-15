from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("singlestock/<int:sid>", views.single_stock, name="singlestock"),
    path("updatestock/<int:sid>", views.update_stock, name="updatestock"),
    path("delete/<int:sid>", views.delete_stock, name="deletestock"),
]
