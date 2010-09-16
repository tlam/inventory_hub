import simplejson

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from customers.forms import CustomerForm
from customers.models import Customer
from histories.models import History


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
            History.created_history(customer, request.user)
            return redirect('customers:update', customer.pk)
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
            past_customer = Customer.objects.get(id=customer_id)
            updated_customer = form.save()
            History.updated_history(past_customer, updated_customer, request.user)
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


def customer_number_ajax(request):
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    value = '%s/%s/%i' %  (first_name[:3].upper(), last_name[:3].upper(), 2)
    data = simplejson.dumps(value)
    return HttpResponse(data, mimetype="application/javascript")
