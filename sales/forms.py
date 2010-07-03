from django import forms
from django.forms import ModelForm

from sales.models import CashSale, CreditSale
from utils.widgets import CalendarField


class CashSaleForm(ModelForm):
    date = CalendarField()

    class Meta:
        model = CashSale


class CreditSaleForm(ModelForm):
    date = CalendarField()

    class Meta:
        model = CreditSale


def sale_form(sale_type, *args, **kwargs):
    if sale_type == 'cash':
        return CashSaleForm(*args, **kwargs)
    else:
        return CreditSaleForm(*args, **kwargs)
