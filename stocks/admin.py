from django.contrib import admin

from stocks.models import Category, Price, Stock, Warehouse

admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Stock)
admin.site.register(Warehouse)
