from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from suppliers.forms import SupplierForm

def index(request):
    data = {}

    return render_to_response(
        'suppliers/index.html',
        data,
        context_instance=RequestContext(request),
    )

def create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
    else:
        form = SupplierForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'suppliers/create.html',
        data,
        context_instance=RequestContext(request),
    )

def update(request):
    data = {}

    return render_to_response(
        'suppliers/update.html',
        data,
        context_instance=RequestContext(request),
    )
