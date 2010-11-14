import json

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.html import escape

from contacts.models import ContactList
from geography.models import Country
from histories.models import History
from suppliers.forms import ForeignSupplierForm, LocalSupplierForm
from suppliers.models import LocalSupplier, ForeignSupplier, SupplierFactory
from utils.tools import capwords


def base_index(request):
    data = {}

    return render_to_response(
        'suppliers/index.html',
        data,
        context_instance=RequestContext(request),
    )


def index(request, supplier_type):
    instance = SupplierFactory.create(supplier_type)
    suppliers = instance.objects.all()
    data = {
        'suppliers': suppliers,
    }

    return render_to_response(
        'suppliers/%s/index.html' % supplier_type,
        data,
        context_instance=RequestContext(request),
    )


def create_foreign(request):
    if request.method == 'POST':
        contacts = ContactList.post_dict(request.POST)
        form = ForeignSupplierForm(request.POST)
        if form.is_valid():
            foreign_supplier = form.save()
            msg = foreign_supplier.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
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
        contacts = {}
        form = ForeignSupplierForm()

    data = {
        'contacts': contacts,
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
        contacts = foreign_supplier.contact_list.post_dict(request.POST)
        form = ForeignSupplierForm(request.POST, instance=foreign_supplier)
        if form.is_valid():
            past_supplier = ForeignSupplier.objects.get(pk=supplier_id)
            updated_supplier = form.save()
            msg = updated_supplier.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
            History.updated_history(past_supplier, updated_supplier, request.user)
            messages.success(request, 'Foreign Supplier updated')
    else:
        contacts = foreign_supplier.contact_list.get_dict()
        form = ForeignSupplierForm(initial=initial_data, instance=foreign_supplier)
    
    data = {
        'contacts': contacts,
        'foreign_supplier': foreign_supplier,
        'form': form,
    }

    return render_to_response(
        'suppliers/foreign/update.html',
        data,
        context_instance=RequestContext(request),
    )


def create_local(request):
    if request.method == 'POST':
        contacts = ContactList.post_dict(request.POST)
        form = LocalSupplierForm(request.POST)
        if form.is_valid():
            local_supplier = form.save()
            msg = local_supplier.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
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
        contacts = {}
        form = LocalSupplierForm()

    data = {
        'contacts': contacts,
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
        contacts = local_supplier.contact_list.post_dict(request.POST)
        form = LocalSupplierForm(request.POST, instance=local_supplier)
        if form.is_valid():
            past_supplier = LocalSupplier.objects.get(pk=supplier_id)
            updated_supplier = form.save()
            msg = updated_supplier.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
            History.updated_history(past_supplier, updated_supplier, request.user)
            messages.success(request, 'Local Supplier updated')
    else:
        contacts = local_supplier.contact_list.get_dict()
        form = LocalSupplierForm(initial=initial_data, instance=local_supplier)
    
    data = {
        'contacts': contacts,
        'form': form,
        'local_supplier': local_supplier,
    }

    return render_to_response(
        'suppliers/local/update.html',
        data,
        context_instance=RequestContext(request),
    )


def delete(request, supplier_type):
    supplier_id = int(request.POST.get('entry_id', 0))
    instance = SupplierFactory.create(supplier_type)
    label = capwords(supplier_type)

    try:
        supplier = instance.objects.get(pk=supplier_id)
        supplier.delete()
        messages.success(request, '%s Supplier deleted' % label)
    except instance.DoesNotExist:
        messages.error(request, '%s Supplier with id %i does not exist' % (label, supplier_id))

    if supplier_type == 'foreign':
        data = reverse('suppliers:index-foreign')
    else:
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
    data = json.dumps(value)
    return HttpResponse(data, mimetype='application/javascript')
