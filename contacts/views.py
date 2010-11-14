import json
import re

from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from contacts.forms import ContactForm
from contacts.models import Email, Phone


def add_email(request):
    contact_index = int(request.GET.get('contact_index', 0))
    email_index = int(request.GET.get('email_index', 0))
    email_index += 1
    data = {
        'i': contact_index,
        'j': email_index,
        'email_choices': Email.EMAIL_CHOICES,
    }

    return render_to_response(
        'contacts/email.html',
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


def add_phone(request):
    contact_index = int(request.GET.get('contact_index', 0))
    phone_index = int(request.GET.get('phone_index', 0))
    phone_index += 1
    data = {
        'i': contact_index,
        'j': phone_index,
        'phone_choices': Phone.PHONE_CHOICES,
    }

    return render_to_response(
        'contacts/phone.html',
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


def add_contact(request):
    last_id = int(request.GET.get('last_id', 0))
    last_id += 1
    data = {
        'i': last_id,
        'email_choices': Email.EMAIL_CHOICES,
        'phone_choices': Phone.PHONE_CHOICES,
    }

    return render_to_response(
        'contacts/contact.html',
        data,
        context_instance=RequestContext(request),
    )

