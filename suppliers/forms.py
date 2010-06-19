from django import forms
from django.forms import ModelForm

from geography.models import City, Country
from suppliers.models import Supplier


class SupplierForm(ModelForm):
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = Supplier

    def clean_city(self):
        data = self.cleaned_data['city']
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = City.objects.get_or_create(name=data)
        return obj
    
    def clean_country(self):
        data = self.cleaned_data['country']
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = Country.objects.get_or_create(name=data)
        return obj
