from django.contrib import admin

from stock_carts.models import StockCart, StockCartItem


class StockCartItemInline(admin.TabularInline):
    model = StockCartItem


class StockCartAdmin(admin.ModelAdmin):
    inlines = [
        StockCartItemInline,
    ]

admin.site.register(StockCart, StockCartAdmin)
