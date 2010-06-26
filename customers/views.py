from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from customers.forms import CustomerForm
from customers.models import Customer

def index(request):
    customers = Customer.objects.all()

    data = {
        'customers': customers,
    }

    return render_to_response(
        'customers/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customers:update', customers.pk)
    else:
        form = CustomerForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'customers/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    initial_data = {
        'city': customer.city.name,
        'country': customer.country.name,
    }

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated')
    else:
        form = CustomerForm(initial=initial_data, instance=customer)

    data = {
        'form': form,
    }

    return render_to_response(
        'customers/update.html',
        data,
        context_instance=RequestContext(request),
    )
