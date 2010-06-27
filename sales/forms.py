from django import forms
from django.forms import ModelForm

from sales.models import CashSale, CreditSale


class CashSaleForm(ModelForm):
    class Meta:
        model = CashSale


class CreditSaleForm(ModelForm):
    class Meta:
        model = CreditSale
