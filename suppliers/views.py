from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.html import escape

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
            if '_popup' in request.GET:
                popup_data = {
                    'obj': escape(foreign_supplier),
                    'pk_value': escape(foreign_supplier.id),
                }
                return render_to_response(
                    'home/close_popup.html',
                    popup_data,
                    context_instance=RequestContext(request),
                )

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
        'foreign_supplier': foreign_supplier,
        'form': form,
    }

    return render_to_response(
        'suppliers/foreign/update.html',
        data,
        context_instance=RequestContext(request),
    )


def index_local(request):
    local_suppliers = LocalSupplier.objects.all()
    data = {
        'local_suppliers': local_suppliers,
    }

    return render_to_response(
        'suppliers/local/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create_local(request):
    if request.method == 'POST':
        form = LocalSupplierForm(request.POST)
        if form.is_valid():
            local_supplier = form.save()
            History.created_history(local_supplier, request.user)
            messages.success(request, 'Local Supplier created.')
            if '_popup' in request.GET:
                popup_data = {
                    'obj': escape(local_supplier),
                    'pk_value': escape(local_supplier.id),
                }
                return render_to_response(
                    'home/close_popup.html',
                    popup_data,
                    context_instance=RequestContext(request),
                )
            return redirect('suppliers:update-local', local_supplier.pk)
    else:
        form = LocalSupplierForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'suppliers/local/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update_local(request, supplier_id):
    local_supplier = get_object_or_404(LocalSupplier, id=supplier_id)
    initial_data = {
        'city': local_supplier.city.name,
    }

    if request.method == 'POST':
        form = LocalSupplierForm(request.POST, instance=local_supplier)
        if form.is_valid():
            past_supplier = LocalSupplier.objects.get(id=supplier_id)
            updated_supplier = form.save()
            History.updated_history(past_supplier, updated_supplier, request.user)
            messages.success(request, 'Local Supplier updated')
    else:
        form = LocalSupplierForm(initial=initial_data, instance=local_supplier)
    
    data = {
        'form': form,
        'local_supplier': local_supplier,
    }

    return render_to_response(
        'suppliers/local/update.html',
        data,
        context_instance=RequestContext(request),
    )
