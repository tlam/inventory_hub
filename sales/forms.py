from django import forms
from django.forms import ModelForm

from sales.models import CashSale, CreditSale


class CashSaleForm(ModelForm):
    class Meta:
        model = CashSale


class CreditSaleForm(ModelForm):
    class Meta:
        model = CreditSale


def sale_form(sale_type, *args, **kwargs):
    if sale_type == 'cash':
        return CashSaleForm(*args, **kwargs)
    else:
        return CreditSaleForm(*args, **kwargs)
