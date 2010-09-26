from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from contacts.forms import ContactForm


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
