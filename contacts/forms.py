from django import forms

from customers.models import Customer


class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer
