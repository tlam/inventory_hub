from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from stocks.forms import StockForm
from stocks.models import Category


def index(request):
    data = {}

    return render_to_response(
        'stocks/index.html',
        data,
        context_instance=RequestContext(request),
    )

def create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
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

def update(request):
    data = {}

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
