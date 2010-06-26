from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils import simplejson

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
    initial_data = {
        'category': stock.category.name,
        'country': stock.country.name,
    }

    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated')
    else:
        form = StockForm(initial=initial_data, instance=stock)

    data = {
        'form': form,
    }

    return render_to_response(
        'stocks/update.html',
        data,
        context_instance=RequestContext(request),
    )


def search_category(request):
    category = request.GET.get('term', '')
    categories = Category.objects.filter(name__icontains=category)
    categories = categories.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(categories))
    return HttpResponse(data, mimetype="application/javascript")
