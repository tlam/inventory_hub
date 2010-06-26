from django import forms
from django.forms import ModelForm

from geography.models import Country
from stocks.models import Category, Stock


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class StockForm(ModelForm):
    category = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Stock

    def clean_category(self):
        data = self.cleaned_data['category']
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = Category.objects.get_or_create(name=data)
        return obj

    def clean_country(self):
        data = self.cleaned_data['country']
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = Country.objects.get_or_create(name=data)
        return obj
