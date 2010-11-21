from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from contacts.models import ContactList
from companies.forms import CompanyForm
from companies.models import Company


def index(request):
    companies = Company.objects.all()

    data = {
        'companies': companies,
    }

    return render_to_response(
        'companies/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        contacts = ContactList.post_dict(request.POST)
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            msg = company.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
            messages.success(request, 'Company created')
            return redirect('companies:update', company.pk)
    else:
        contacts = {}
        form = CompanyForm()

    data = {
        'contacts': contacts,
        'form': form,
    }

    return render_to_response(
        'companies/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        contacts = customer.contact_list.post_dict(request.POST)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            updated_company = form.save()
            msg = updated_company.contact_list.update_contacts(contacts)
            if msg:
                messages.warning(request, msg)
            messages.success(request, 'Company updated.')
    else:
        try:
            contacts = company.contact_list.get_dict()
        except AttributeError:
            company.save()
            contacts = {}
        form = CompanyForm(instance=company)

    data = {
        'contacts': contacts,
        'company': company,
        'form': form,
    }

    return render_to_response(
        'companies/update.html',
        data,
        context_instance=RequestContext(request),
    )


def delete(request):
    company_id = int(request.POST.get('entry_id', 0))
    try:
        company = Company.objects.get(pk=company_id)
        company.delete()
        messages.success(request, 'Company deleted')
    except Company.DoesNotExist:
        messages.error(request, 'Company with id %i does not exist' % company_id)
    data = reverse('companies:index')
    return HttpResponse(data, mimetype="application/javascript")
