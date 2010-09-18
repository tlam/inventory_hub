from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from customers.forms import CustomerForm
from customers.models import Customer
from histories.models import History
from quotations.forms import QuotationForm
from quotations.models import Quotation
from stocks.models import StockItem


def index(request):
    quotations = Quotation.objects.all()

    data = {
        'quotations': quotations,
    }

    return render_to_response(
        'quotations/index.html',
        data,
        context_instance=RequestContext(request),
    )


def customer(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            History.created_history(customer, request.user)
            return redirect('quotations:create', customer.pk)
    else:
        form = CustomerForm()

    data = {
        'customers': customers,
        'form': form,
    }

    return render_to_response(
        'quotations/customer.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save()
            History.created_history(quotation, request.user)
            messages.success(request, 'Quotation created.')
            return redirect('quotations:update', quotation.pk)
    else:
        form = QuotationForm(initial={'customer': customer_id})

    data = {
        'form': form,
    }

    return render_to_response(
        'quotations/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    StockItemFormSet = inlineformset_factory(Quotation, StockItem, extra=1, fields = ('stock', 'quantity', 'discount',))

    if request.method == 'POST':
        form = QuotationForm(request.POST, instance=quotation)
        formset = StockItemFormSet(request.POST, instance=quotation)
        if form.is_valid() and formset.is_valid():
            past_quotation = Quotation.objects.get(id=quotation_id)
            past_items = StockItem.objects.items_info(past_quotation)
            updated_quotation = form.save()
            History.updated_history(past_quotation, updated_quotation, request.user)
            formset.save()
            updated_items = StockItem.objects.items_info(updated_quotation)
            History.updated_list_history(past_items, updated_items, request.user)
            messages.success(request, 'Quotation updated.')
            """
            Redirecting will force an update of the current page and
            add an extra row
            """
            return redirect('quotations:update', quotation_id)
    else:
        formset = StockItemFormSet(instance=quotation)
        form = QuotationForm(instance=quotation)

    data = {
        'form': form,
        'formset': formset,
    }

    return render_to_response(
        'quotations/update.html',
        data,
        context_instance=RequestContext(request),
    )
