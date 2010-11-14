from django import forms
from django.forms import ModelForm

from customers.models import Customer
from geography.models import City


class CustomerForm(ModelForm):
    city = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Customer
        exclude = ('contact_list',)

    def clean_city(self):
        data = self.cleaned_data['city']
        if data.isdigit():
            raise forms.ValidationError('Digits are not allowed')
        if data.isupper():
            raise forms.ValidationError('Use CamelCase instead of UPPERCASE')
        obj, created = City.objects.get_or_create(name=data)
        return obj

    def clean_business_registration_number(self):
        company = self.cleaned_data.get('company_name', '')
        brn = self.cleaned_data['business_registration_number']
        if company and not brn:
            raise forms.ValidationError('Please enter your business \
                registration number if you have a company')
        return brn
