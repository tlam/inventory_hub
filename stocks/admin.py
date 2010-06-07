from django.contrib import admin

from stocks.models import Category, Price, Warehouse

admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Warehouse)


