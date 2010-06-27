from django.contrib import admin

from sales.models import CashSale, CreditSale
from stocks.models import StockItem


class StockItemInline(admin.TabularInline):
    model = StockItem


class SaleAdmin(admin.ModelAdmin):
    inlines = [
        StockItemInline,
    ]

admin.site.register(CashSale, SaleAdmin)
admin.site.register(CreditSale)
