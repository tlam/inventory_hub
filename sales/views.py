from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from customers.forms import CustomerForm
from customers.models import Customer
from histories.models import History
from sales.forms import sale_form
from sales.models import CashSale, CreditSale


def index(request):
    cash_sales = CashSale.objects.all()
    credit_sales = CreditSale.objects.all()

    data = {
        'cash_sales': cash_sales,
        'credit_sales': credit_sales,
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
            History.created_history(customer, request.user)
            return redirect('sales:create', sale_type, customer.pk)
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
        form = sale_form(sale_type, request.POST)
        if form.is_valid():
            sale = form.save()
            History.created_history(sale, request.user)
            messages.success(request, 'Sale created')
            return redirect('sales:update', sale_type, sale.pk)
    else:
        form = sale_form(sale_type, initial={'customer': customer.pk})

    data = {
        'form': form,
        'sale_type': sale_type,
    }

    return render_to_response(
        'sales/create.html',
        data,
        context_instance=RequestContext(request),
    )
    

def update(request, sale_type, sale_id):
    if sale_type == 'cash':
        instance = CashSale
    else:
        instance = CreditSale

    sale = get_object_or_404(instance, pk=sale_id)

    if request.method == 'POST':
        contacts = sale.contact_list.post_dict(request.POST)
        form = sale_form(sale_type, request.POST, instance=sale)
        stock_item_code = request.POST.get('stock-item-code', '')

        if stock_item_code:
            msg = sale.cart.add_item(stock_item_code)
            if msg.get('success', ''):
                messages.success(request, msg.get('success', ''))
            else:
                messages.warning(request, msg.get('warning', ''))
        else:
            if form.is_valid():
                form.save()
                sale.cart.update_items(request.POST)
                messages.success(request, 'Sale updated')

        msg = sale.contact_list.update_contacts(contacts)
        if msg:
            messages.warning(request, msg)
    else:
        try:
            contacts = sale.contact_list.get_dict()
        except AttributeError:
            sales.save()
            contacts = {}
        form = sale_form(sale_type, instance=sale)

    stock_items = sale.cart.stockcartitem_set.all()

    data = {
        'cart': sale.cart,
        'contacts': contacts,
        'form': form,
        'price_type': sale.customer.price_type,
        'sale': sale,
        'sale_type': sale_type,
        'stock_items': stock_items,
    }

    return render_to_response(
        'sales/update.html',
        data,
        context_instance=RequestContext(request),
    )


def delete(request, sale_type):
    sale_id = int(request.POST.get('entry_id', 0))
    try:
        if sale_type == 'cash':
            sale = CashSale.objects.get(pk=sale_id)
        else:
            sale = CreditSale.objects.get(pk=sale_id)
        sale.delete() 
        messages.success(request, 'Sale deleted')
    except:
        messages.error(request, 'Sale with id %i does not exist' % sale_id)

    data = reverse('sales:index')
    return HttpResponse(data, mimetype="application/javascript")
