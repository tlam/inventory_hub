from django.contrib import messages
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from customers.models import Customer
from quotations.forms import QuotationForm


def index(request):
    data = {}
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
            sale = form.save()
            return redirect('sales:update', sale_type, sale.pk)
    else:
        form = QuotationForm(initial={'customer': customer.pk})

    data = {
        'form': form,
    }

    return render_to_response(
        'quotations/create.html',
        data,
        context_instance=RequestContext(request),
    )
