from django.contrib import admin

from sales.models import CashSale, CreditSale


class SaleAdmin(admin.ModelAdmin):
    pass

admin.site.register(CashSale, SaleAdmin)
admin.site.register(CreditSale, SaleAdmin)
