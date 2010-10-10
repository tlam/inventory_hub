import json
import re

from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from contacts.forms import ContactForm
from contacts.models import Email, Phone


def ajax_add_email(request):
    last_id = int(request.GET.get('last_id', 0))
    last_id += 1
    data = {
        'email_choices': Email.EMAIL_CHOICES,
        'i': last_id,
    }

    return render_to_response(
        'contacts/ajax_add_email.html',
        data,
        context_instance=RequestContext(request),
    )


def ajax_remove_email(request):
    email_id = int(request.GET.get('email_id', 0))
    if email_id:
        try:
            Email.objects.get(pk=email_id).delete()
        except Email.DoesNotExist:
            pass
    data = json.dumps({})
    return HttpResponse(data, mimetype='application/javascript')


def post_emails(post_list):
    email_dict = {}
    for element_id, name in post_list:
        m = re.search('email_set-\d+', element_id)
        if m:
            row_id = m.group(0)
            if not row_id in email_dict:
                email_dict[row_id] = {}

            address_match = re.search('\d+-address', element_id)
            type_match = re.search('\d+-type', element_id)
            email_id = re.search('\d+-pk', element_id)

            if address_match:
                address_dict = {'address': name[0]}
                email_dict[row_id].update(address_dict)
            elif type_match:
                type_dict = {'email_type': name[0]}
                email_dict[row_id].update(type_dict)
            elif email_id:
                pk_dict = {'id': name[0]}
                email_dict[row_id].update(pk_dict)

    emails_valid = True
    unsorted_email_dict = {}

    # Remove blank entries
    for row_id, email in email_dict.items():
        if email['address'] or email['email_type']:
            unsorted_email_dict[row_id] = email

        if not email['address'] or not email['email_type']:
            emails_valid = False

    email_dict = sorted(unsorted_email_dict.items())
    print email_dict

    # Validate emails to True if none entered
    if not email_dict:
        emails_valid = True

    return emails_valid, email_dict


def create_emails(customer, email_dict):
    for row_id, email in email_dict:
        address = email['address']
        email_type = email['email_type']
        email_id = int(email.get('id', 0))
        if email_id:
            existing_email = Email.objects.get(pk=email_id)
            existing_email.address = address
            existing_email.email_type = email_type
            existing_email.save()
        else:
            Email.objects.create(customer=customer, address=address, \
                email_type=email_type)


def ajax_add_phone(request):
    last_id = int(request.GET.get('last_id', 0))
    last_id += 1
    data = {
        'i': last_id,
        'phone_choices': Phone.PHONE_CHOICES,
    }

    return render_to_response(
        'contacts/ajax_add_phone.html',
        data,
        context_instance=RequestContext(request),
    )


def ajax_remove_phone(request):
    phone_id = int(request.GET.get('phone_id', 0))
    if phone_id:
        try:
            Phone.objects.get(pk=phone_id).delete()
        except Phone.DoesNotExist:
            pass
    data = json.dumps({})
    return HttpResponse(data, mimetype='application/javascript')


def post_phones(post_list):
    phone_dict = {}
    for element_id, name in post_list:
        m = re.search('phone_set-\d+', element_id)
        if m:
            row_id = m.group(0)
            if not row_id in phone_dict:
                phone_dict[row_id] = {}

            number_match = re.search('\d+-number', element_id)
            type_match = re.search('\d+-type', element_id)
            phone_id = re.search('\d+-pk', element_id)

            if number_match:
                number_dict = {'number': name[0]}
                phone_dict[row_id].update(number_dict)
            elif type_match:
                type_dict = {'phone_type': name[0]}
                phone_dict[row_id].update(type_dict)
            elif phone_id:
                pk_dict = {'id': name[0]}
                phone_dict[row_id].update(pk_dict)

    phones_valid = True
    unsorted_phone_dict = {}

    # Remove blank entries
    for row_id, phone in phone_dict.items():
        if phone['number'] or phone['phone_type']:
            unsorted_phone_dict[row_id] = phone

        if not phone['number'] or not phone['phone_type']:
            phones_valid = False

    phone_dict = sorted(unsorted_phone_dict.items())

    # Validate phones to True if none entered
    if not phone_dict:
        phones_valid = True

    return phones_valid, phone_dict


def create_phones(customer, phone_dict):
    for row_id, phone in phone_dict:
        number = phone['number']
        phone_type = phone['phone_type']
        phone_id = int(phone.get('id', 0))
        if phone_id:
            existing_phone = Phone.objects.get(pk=phone_id)
            existing_phone.number = number
            existing_phone.phone_type = phone_type
            existing_phone.save()
        else:
            Phone.objects.create(customer=customer, number=number, \
                phone_type=phone_type)
