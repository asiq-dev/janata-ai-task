from django.contrib import admin

# Register your models here.
from .models import Stock
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class StockResource(resources.ModelResource):
    class Meta:
        model = Stock


class StockAdmin(ImportExportModelAdmin):
    resource_class = StockResource


admin.site.register(Stock, StockAdmin)
