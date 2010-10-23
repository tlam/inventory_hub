from django.contrib import messages
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
        form = sale_form(sale_type, request.POST, instance=sale)
        if 'add-stock-item' in request.POST:
            stock_item_code = request.POST.get('stock-item-code', '')
            msg = sale.cart.add_item(stock_item_code)
            if msg.get('success', ''):
                messages.success(request, msg.get('success', ''))
            else:
                messages.warning(request, msg.get('warning', ''))
        else:
            if form.is_valid():
                past_sale = instance.objects.get(pk=sale_id)
                updated_sale = form.save()
                updated_sale.cart.update_items(request.POST)
                History.updated_history(past_sale, updated_sale, request.user)
                messages.success(request, '%s sale updated' % sale_type)
    else:
        form = sale_form(sale_type, instance=sale)

    stock_items = sale.cart.stockcartitem_set.all()

    data = {
        'form': form,
        'sale': sale,
        'sale_type': sale_type,
        'stock_items': stock_items,
    }

    return render_to_response(
        'sales/update.html',
        data,
        context_instance=RequestContext(request),
    )


def update2(request, sale_type, sale_id):
    if sale_type == 'cash':
        instance = CashSale
    else:
        instance = CreditSale

    sale = get_object_or_404(instance, pk=sale_id)
    StockItemFormSet = inlineformset_factory(instance, StockItem, extra=1, fields = ('stock', 'quantity', 'discount',))

    if request.method == 'POST':
        form = sale_form(sale_type, request.POST, instance=sale)
        formset = StockItemFormSet(request.POST, instance=sale)
        if form.is_valid() and formset.is_valid():
            past_sale = instance.objects.get(id=sale_id)
            past_items = StockItem.objects.items_info(past_sale)
            updated_sale = form.save()
            History.updated_history(past_sale, updated_sale, request.user)
            formset.save()
            updated_items = StockItem.objects.items_info(updated_sale)
            History.updated_list_history(past_items, updated_items, request.user)
            messages.success(request, '%s sale updated' % sale_type)
            """
            Redirecting will force an update of the current page and
            add an extra row
            """
            return redirect('sales:update', sale_type, sale_id)
    else:
        formset = StockItemFormSet(instance=sale)
        form = sale_form(sale_type, instance=sale)

    data = {
        'form': form,
        'formset': formset,
        'sale_type': sale_type,
    }

    return render_to_response(
        'sales/update.html',
        data,
        context_instance=RequestContext(request),
    )
