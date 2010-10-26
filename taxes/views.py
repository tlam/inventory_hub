from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from taxes.forms import TaxForm
from taxes.models import Tax


def index(request):
    taxes = Tax.objects.all()

    data = {
        'taxes': taxes,
    }

    return render_to_response(
        'taxes/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            tax = form.save()
            messages.success(request, 'Tax created')
            return redirect('taxes:update', tax.pk)
    else:
        form = TaxForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'taxes/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request, tax_id):
    tax = get_object_or_404(Tax, pk=tax_id)

    if request.method == 'POST':
        form = TaxForm(request.POST, instance=tax)
        if form.is_valid():
            updated_tax = form.save()
            messages.success(request, 'Tax updated.')
    else:
        form = TaxForm(instance=tax)

    data = {
        'tax': tax,
        'form': form,
    }

    return render_to_response(
        'taxes/update.html',
        data,
        context_instance=RequestContext(request),
    )


def delete(request):
    tax_id = int(request.POST.get('entry_id', 0))
    try:
        tax = Tax.objects.get(pk=tax_id)
        tax.delete()
        messages.success(request, 'Tax deleted')
    except Tax.DoesNotExist:
        messages.error(request, 'Tax with id %i does not exist' % tax_id)
    data = reverse('taxes:index')
    return HttpResponse(data, mimetype="application/javascript")
