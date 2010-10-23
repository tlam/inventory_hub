from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from histories.models import History
from stocks.forms import StockForm
from stocks.models import Category, Stock


def index(request):
    stocks = Stock.objects.all()

    data = {
        'stocks': stocks,
    }

    return render_to_response(
        'stocks/index.html',
        data,
        context_instance=RequestContext(request),
    )

def create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save()
            History.created_history(stock, request.user)
            messages.success(request, 'Stock created.')
            return redirect('stocks:update', stock.pk)
    else:
        form = StockForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'stocks/create.html',
        data,
        context_instance=RequestContext(request),
    )

def update(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)

    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            past_stock = Stock.objects.get(pk=stock_id)
            updated_stock = form.save()
            History.updated_history(past_stock, updated_stock, request.user)
            messages.success(request, 'Stock updated.')
    else:
        form = StockForm(instance=stock)

    data = {
        'form': form,
        'stock': stock,
    }

    return render_to_response(
        'stocks/update.html',
        data,
        context_instance=RequestContext(request),
    )


def delete(request):
    stock_id = int(request.POST.get('entry_id', 0))
    try:
        stock = Stock.objects.get(pk=stock_id)
        stock.delete() 
        messages.success(request, 'Stock deleted')
    except Stock.DoesNotExist:
        messages.error(request, 'Stock with id %i does not exist' % customer_id)
    data = reverse('stocks:index')
    return HttpResponse(data, mimetype="application/javascript")


def search_category(request):
    """
    AJAX autocomplete of category name.
    """
    category = request.GET.get('term', '')
    categories = Category.objects.filter(name__icontains=category)
    categories = categories.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(categories))
    return HttpResponse(data, mimetype="application/javascript")


def search_stock(request):
    description = request.GET.get('term', '')
    stocks = Stock.objects.filter(description__istartswith=description)
    stock_list = []
    for stock in stocks:
        stock_list.append({
            'label': stock.item_code,
            'desc': stock.description,
        })
    #stocks = stocks.values_list('item_code', flat=True).order_by('item_code')
    #data = simplejson.dumps(list(stocks))
    data = simplejson.dumps(stock_list)
    print data
    return HttpResponse(data, mimetype="application/javascript")
