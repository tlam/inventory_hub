import json

from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from contacts.views import create_emails, post_emails
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
        post_list = request.POST.lists()
        emails_valid, email_dict = post_emails(post_list)
        form = CustomerForm(request.POST)
        if form.is_valid() and emails_valid:
            customer = form.save()
            History.created_history(customer, request.user)
            messages.success(request, 'Customer created.')
            create_emails(customer, email_dict)
            return redirect('customers:update', customer.pk)
    else:
        email_dict = {}
        form = CustomerForm()

    data = {
        'email_dict': email_dict,
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
    }

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            past_customer = Customer.objects.get(id=customer_id)
            updated_customer = form.save()
            History.updated_history(past_customer, updated_customer, request.user)
            messages.success(request, 'Customer updated.')
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
    # TODO: need pass customer id or 0
    try:
        customer = Customer.objects.get(first_name=first_name, last_name=last_name)
        customer_id = customer.pk
    except Customer.DoesNotExist:
        max_id = Customer.objects.aggregate(Max('id'))
        max_id = max_id.get('id__max', 0)
        if not max_id:
            max_id = 0
        customer_id = max_id + 1
    value = '%s/%s/%i' %  (first_name[:3].upper(), last_name[:3].upper(), customer_id)
    data = json.dumps(value)
    return HttpResponse(data, mimetype="application/javascript")
