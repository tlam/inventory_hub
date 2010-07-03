from django.contrib import admin

from quotations.models import Quotation
from stocks.models import StockItem


class StockItemInline(admin.TabularInline):
    model = StockItem
    extra = 1


class QuotationAdmin(admin.ModelAdmin):
    inlines = [
        StockItemInline,
    ]

admin.site.register(Quotation, QuotationAdmin)
