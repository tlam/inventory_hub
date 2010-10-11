from django import forms
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory

from geography.models import Country
from stocks.models import Category, Stock, StockItem


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class StockForm(ModelForm):
    class Meta:
        model = Stock


class InlineStockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ('category', 'item_code', 'description',)


class BaseStockFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        # allow the super class to create the fields as usual
        super(BaseStockFormset, self).add_fields(form, index)
 
        # created the nested formset
        try:
            instance = self.get_queryset()[index]
            stock = instance.stock
            pk_value = stock.pk
        except IndexError:
            stock = None
            pk_value = hash(form.prefix)
 
        # store the formset in the .nested property
        form.nested = [
            InlineStockForm(
                data=self.data,
                instance=stock,
                prefix='STOCK_%s' % pk_value,
            )
        ]
