from django import forms
from django.forms import ModelForm

from quotations.models import Quotation
from utils.widgets import CalendarField

class QuotationForm(ModelForm):
    date = CalendarField()

    class Meta:
        model = Quotation
