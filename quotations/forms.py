from django import forms
from django.forms import ModelForm

from quotations.models import Quotation


class QuotationForm(ModelForm):

    class Meta:
        model = Quotation
