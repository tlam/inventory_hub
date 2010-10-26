from django.forms import ModelForm

from taxes.models import Tax


class TaxForm(ModelForm):
    class Meta:
        model = Tax
