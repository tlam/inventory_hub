import re

from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from contacts.forms import ContactForm
from contacts.models import Email


def add(request):
    print request.GET
    print request.POST
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    data = {
       'form': form,
       'num_emails': range(1),
    }

    return render_to_response(
        'contacts/add.html',
        data,
        context_instance=RequestContext(request),
    )


def ajax_email(request):
    print request.POST
    num = int(request.POST.get('num_emails', 0))
    num += 1
    data = {
        'num_emails': range(num),
    }
    return render_to_response(
        'contacts/ajax_email.html',
        data,
        context_instance=RequestContext(request),
    )


def ajax_add_email(request):
    last_id = int(request.GET.get('last_id', 0))
    last_id += 1
    data = {
        'i': last_id,
    }

    return render_to_response(
        'contacts/ajax_add_email.html',
        data,
        context_instance=RequestContext(request),
    )


def ajax_remove_email(request):
    removed_id = int(request.POST.get('removed_id', 0))
    num = int(request.POST.get('num_emails', 0))
    num_emails = range(num)
    num_emails.remove(removed_id)
    data = {
        'num_emails': num_emails,
    }
    return render_to_response(
        'contacts/ajax_email.html',
        data,
        context_instance=RequestContext(request),
    )


def post_emails(post_list):
    email_dict = {}
    for element_id, name in post_list:
        m = re.search('\d+', element_id)
        if m:
            row_id = m.group(0)
            if not row_id in email_dict:
                email_dict[row_id] = {}

            address_match = re.search('\d+-address', element_id)
            type_match = re.search('\d+-type', element_id)
            email_id = re.search('\d+-id', element_id)

            if address_match:
                address_dict = {'address': name[0]}
                email_dict[row_id].update(address_dict)
            elif type_match:
                type_dict = {'email_type': name[0]}
                email_dict[row_id].update(type_dict)
            elif email_id:
                id_dict = {'id': name[0]}
                email_dict[row_id].update(id_dict)

    emails_valid = True
    unsorted_email_dict = {}

    # Remove blank entries
    for row_id, email in email_dict.items():
        if email['address'] or email['email_type']:
            unsorted_email_dict[row_id] = email

        if not email['address'] or not email['email_type']:
            emails_valid = False

    email_dict = sorted(unsorted_email_dict.items())

    return emails_valid, email_dict


def create_emails(customer, email_dict):
    for row_id, email in email_dict:
        address = email['address']
        email_type = email['email_type']
        email_id = int(email.get('id', 0))
        if email_id:
            existing_email = Email.objects.get(id=email_id)
            existing_email.address = address
            existing_email.email_type = email_type
            existing_email.save()
        else:
            Email.objects.create(customer=customer, address=address, email_type=email_type)

