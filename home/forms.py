from django.forms import ModelForm

from home.models import Home


class HomeForm(ModelForm):
    class Meta:
        model = Home
