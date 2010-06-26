from django.contrib import admin

from sales.models import CashSale, CreditSale

admin.site.register(CashSale)
admin.site.register(CreditSale)
