from django import forms
from django.forms import ModelForm

from sales.models import CashSale, CreditSale
from utils.widgets import CalendarField


class BaseSaleForm(ModelForm):
    date = CalendarField()


class CashSaleForm(BaseSaleForm):
    class Meta:
        model = CashSale
        exclude = ('cart', 'contact_list')


class CreditSaleForm(BaseSaleForm):
    class Meta:
        model = CreditSale
        exclude = ('cart', 'contact_list')


def sale_form(sale_type, *args, **kwargs):
    if sale_type == 'cash':
        return CashSaleForm(*args, **kwargs)
    else:
        return CreditSaleForm(*args, **kwargs)
