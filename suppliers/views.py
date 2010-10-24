import json

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.html import escape

from geography.models import Country
from histories.models import History
from suppliers.forms import ForeignSupplierForm, LocalSupplierForm
from suppliers.models import LocalSupplier, ForeignSupplier, SupplierFactory


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
    foreign_supplier = get_object_or_404(ForeignSupplier, pk=supplier_id)
    initial_data = {
        'city': foreign_supplier.city.name,
    }

    if request.method == 'POST':
        form = ForeignSupplierForm(request.POST, instance=foreign_supplier)
        if form.is_valid():
            past_supplier = ForeignSupplier.objects.get(pk=supplier_id)
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


def delete_foreign(request):
    supplier_id = int(request.POST.get('entry_id', 0))
    try:
        supplier = ForeignSupplier.objects.get(pk=supplier_id)
        supplier.delete() 
        messages.success(request, 'Foreign Supplier deleted')
    except ForeignSupplier.DoesNotExist:
        messages.error(request, 'Foreign Supplier with id %i does not exist' % supplier_id)
    data = reverse('suppliers:index-foreign')
    return HttpResponse(data, mimetype="application/javascript")


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
    local_supplier = get_object_or_404(LocalSupplier, pk=supplier_id)
    initial_data = {
        'city': local_supplier.city.name,
    }

    if request.method == 'POST':
        form = LocalSupplierForm(request.POST, instance=local_supplier)
        if form.is_valid():
            past_supplier = LocalSupplier.objects.get(pk=supplier_id)
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


def delete_local(request):
    supplier_id = int(request.POST.get('entry_id', 0))
    try:
        supplier = LocalSupplier.objects.get(pk=supplier_id)
        supplier.delete() 
        messages.success(request, 'Local Supplier deleted')
    except LocalSupplier.DoesNotExist:
        messages.error(request, 'Local Supplier with id %i does not exist' % supplier_id)
    data = reverse('suppliers:index-local')
    return HttpResponse(data, mimetype="application/javascript")


def supplier_number_ajax(request, supplier_type):
    company_name = request.GET.get('company_name', '')
    country_id = int(request.GET.get('country_id', 0))

    company_name_prefix = company_name[:2].upper()

    suppliers = SupplierFactory.create(supplier_type).objects.filter(
        country=country_id,
        company_name__istartswith=company_name_prefix,
    )

    try:
        country_name = Country.objects.get(pk=country_id).name
    except Country.DoesNotExist:
        country_name = ''

    country_name_prefix = country_name[:3].upper()
    max_id = suppliers.count() + 1
    value = '%s/%s/%03d' % (company_name_prefix, country_name_prefix, max_id)
    print value
    data = json.dumps(value)
    return HttpResponse(data, mimetype='application/javascript')
