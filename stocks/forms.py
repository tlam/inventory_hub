from django import forms
from django.forms import ModelForm

from geography.models import Country
from stocks.models import Category, Stock


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class StockForm(ModelForm):
    class Meta:
        model = Stock
