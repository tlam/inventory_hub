from django import forms
from django.forms import ModelForm

from geography.models import City, Country
from suppliers.models import ForeignSupplier, LocalSupplier


class BaseSupplierForm(ModelForm):
    city = forms.CharField(max_length=100)

    def clean_city(self):
        data = self.cleaned_data['city']
        if data.isdigit():
            raise forms.ValidationError('Digits are not allowed')
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = City.objects.get_or_create(name=data)
        return obj


class ForeignSupplierForm(BaseSupplierForm):
    class Meta:
        model = ForeignSupplier


class LocalSupplierForm(BaseSupplierForm):
    class Meta:
        model = LocalSupplier
