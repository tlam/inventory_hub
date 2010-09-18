from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from histories.models import History
from suppliers.forms import ForeignSupplierForm, LocalSupplierForm
from suppliers.models import LocalSupplier, ForeignSupplier


def index(request):
    data = {}

    return render_to_response(
        'suppliers/index.html',
        data,
        context_instance=RequestContext(request),
    )


def index_foreign(request):
    foreign_suppliers = ForeignSupplier.objects.all()
    data = {
        'foreign_suppliers': foreign_suppliers,
    }

    return render_to_response(
        'suppliers/foreign/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create_foreign(request):
    if request.method == 'POST':
        form = ForeignSupplierForm(request.POST)
        if form.is_valid():
            foreign_supplier = form.save()
            History.created_history(foreign_supplier, request.user)
            messages.success(request, 'Foreign Supplier created.')
            return redirect('suppliers:update-foreign', foreign_supplier.pk)
    else:
        form = ForeignSupplierForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'suppliers/foreign/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update_foreign(request, supplier_id):
    foreign_supplier = get_object_or_404(ForeignSupplier, id=supplier_id)
    initial_data = {
        'city': foreign_supplier.city.name,
    }

    if request.method == 'POST':
        form = ForeignSupplierForm(request.POST, instance=foreign_supplier)
        if form.is_valid():
            past_supplier = ForeignSupplier.objects.get(id=supplier_id)
            updated_supplier = form.save()
            History.updated_history(past_supplier, updated_supplier, request.user)
            messages.success(request, 'Foreign Supplier updated')
    else:
        form = ForeignSupplierForm(initial=initial_data, instance=foreign_supplier)
    
    data = {
        'form': form,
    }

    return render_to_response(
        'suppliers/foreign/update.html',
        data,
        context_instance=RequestContext(request),
    )
