import json

from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from contacts.models import Email, Phone
from contacts.views import create_emails, create_phones, post_emails, post_phones
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
        phones_valid, phone_dict = post_phones(post_list)
        form = CustomerForm(request.POST)
        if form.is_valid() and emails_valid:
            customer = form.save()
            History.created_history(customer, request.user)
            messages.success(request, 'Customer created.')
            create_emails(customer, email_dict)
            return redirect('customers:update', customer.pk)
    else:
        email_dict = {}
        phone_dict = {}
        form = CustomerForm()

    data = {
        'email_choices': Email.EMAIL_CHOICES,
        'email_dict': email_dict,
        'form': form,
        'phone_choices': Phone.PHONE_CHOICES,
        'phone_dict': phone_dict,
    }

    return render_to_response(
        'customers/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    emails = customer.customer_email.order_by('address')
    phones = customer.phone_set.all()


    # translate QueryObject to Python dict?
    initial_data = {
        'city': customer.city.name,
    }

    if request.method == 'POST':
        post_list = request.POST.lists()
        emails_valid, email_dict = post_emails(post_list)
        phones_valid, phone_dict = post_phones(post_list)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid() and emails_valid and phones_valid:
            past_customer = Customer.objects.get(pk=customer_id)
            updated_customer = form.save()
            History.updated_history(past_customer, updated_customer, \
                request.user)
            messages.success(request, 'Customer updated.')
            create_emails(past_customer, email_dict)
            create_phones(past_customer, phone_dict)
    else:
        form = CustomerForm(initial=initial_data, instance=customer)

        email_dict = {}
        i = 0
        for email in emails:
            email_dict[i] = email
            i += 1

        if email_dict:
            email_dict = email_dict.items()

        phone_dict = {}
        i = 0
        for phone in phones:
            phone_dict[i] = phone
            i += 1

        if phone_dict:
            phone_dict = phone_dict.items()

    data = {
        'email_choices': Email.EMAIL_CHOICES,
        'email_dict': email_dict,
        'emails': emails,
        'form': form,
        'phone_choices': Phone.PHONE_CHOICES,
        'phone_dict': phone_dict,
        'phones': phones,
    }

    return render_to_response(
        'customers/update.html',
        data,
        context_instance=RequestContext(request),
    )


def customer_number_ajax(request):
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')

    first_name_prefix = first_name[:3].upper()
    last_name_prefix = last_name[:3].upper()

    customers = Customer.objects.filter(
        first_name__istartswith=first_name_prefix,
        last_name__istartswith=last_name_prefix,
    )

    max_id = customers.count() + 1

    value = '%s/%s/%03d' % (first_name_prefix, last_name_prefix, max_id)

    '''
    try:
        customer = Customer.objects.get(first_name=first_name, \
            last_name=last_name)
        customer_id = customer.pk
    except Customer.DoesNotExist:
        max_id = Customer.objects.aggregate(Max('id'))
        max_id = max_id.get('id__max', 0)
        if not max_id:
            max_id = 0
        customer_id = max_id + 1
    value = '%s/%s/%i' % (first_name[:3].upper(), last_name[:3].upper(), \
        customer_id)
    '''
    data = json.dumps(value)
    return HttpResponse(data, mimetype="application/javascript")
