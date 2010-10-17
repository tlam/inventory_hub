from django.contrib import admin

from stocks.models import Category, Stock


class StockAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Stock, StockAdmin)
