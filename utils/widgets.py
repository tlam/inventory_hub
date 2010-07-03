from django import forms


class CalendarField(forms.DateField):
    widget = forms.DateInput(attrs={'class': 'date-field'})

    def __init__(self, *args, **kwargs):
        super(CalendarField, self).__init__(*args, **kwargs)
