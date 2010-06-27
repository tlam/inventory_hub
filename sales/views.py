from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from customers.forms import CustomerForm
from customers.models import Customer
from sales.forms import CashSaleForm, CreditSaleForm
from sales.models import CashSale, CreditSale


def index(request):
    data = {
    }

    return render_to_response(
        'sales/index.html',
        data,
        context_instance=RequestContext(request),
    )


def customer(request, sale_type):
    customers = Customer.objects.all()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            # redirect to create sales page
            #return redirect('customers:update', customer.pk)
    else:
        form = CustomerForm()

    data = {
        'customers': customers,
        'form': form,
        'sale_type': sale_type,
    }

    return render_to_response(
        'sales/customer.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request, sale_type, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CashSaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            return redirect('sales:update-cash-sale', sale.pk)
    else:
        form = CashSaleForm(initial={'customer': customer.pk})

    data = {
        'form': form,
    }

    return render_to_response(
        'sales/create.html',
        data,
        context_instance=RequestContext(request),
    )
    

def create_cash_sale(request):
    if request.method == 'POST':
        form = CashSaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            return redirect('sales:update-cash-sale', sale.pk)
    else:
        form = CashSaleForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'sales/create_cash_sale.html',
        data,
        context_instance=RequestContext(request),
    )


def update_cash_sale(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)

    if request.method == 'POST':
        form = CashSaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cash sale updated')
    else:
        form = CashSaleForm(instance=supplier)
    
    data = {
        'form': form,
    }

    return render_to_response(
        'sales/update_cash_sale.html',
        data,
        context_instance=RequestContext(request),
    )
