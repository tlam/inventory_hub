from django.forms import ModelForm

from stocks.models import Category, Stock


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class StockForm(ModelForm):
    class Meta:
        model = Stock
