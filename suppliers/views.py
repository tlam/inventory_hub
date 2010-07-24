from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from histories.models import History
from suppliers.forms import SupplierForm
from suppliers.models import Supplier


def index(request):
    suppliers = Supplier.objects.all()
    data = {
        'suppliers': suppliers,
    }

    return render_to_response(
        'suppliers/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            History.created_history(supplier, request.user)
            messages.success(request, 'Supplier created')
            return redirect('suppliers:update', supplier.pk)
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

def update(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    initial_data = {
        'city': supplier.city.name,
        'country': supplier.country.name,
    }

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            past_supplier = Supplier.objects.get(id=supplier_id)
            updated_supplier = form.save()
            History.updated_history(past_supplier, updated_supplier, request.user)
            messages.success(request, 'Supplier updated')
    else:
        form = SupplierForm(initial=initial_data, instance=supplier)
    
    data = {
        'form': form,
    }

    return render_to_response(
        'suppliers/update.html',
        data,
        context_instance=RequestContext(request),
    )
