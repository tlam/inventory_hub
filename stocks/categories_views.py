from django.shortcuts import render_to_response
from django.template import RequestContext

from stocks.forms import CategoryForm
from stocks.models import Category
from utils.tools import capwords


def index(request):
    data = {}

    return render_to_response(
        'stocks/categories/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'stocks/categories/create.html',
        data,
        context_instance=RequestContext(request),
    )


def update(request):
    data = {}

    return render_to_response(
        'stocks/categories/update.html',
        data,
        context_instance=RequestContext(request),
    )


def add_ajax(request):
    new_category = request.POST.get('new_category', '')
    new_category = capwords(new_category)
    if new_category:
        Category.objects.get_or_create(name=new_category)

    data = {
        'categories': Category.objects.order_by('name'),
        'new_category': new_category,
    }

    return render_to_response(
        'stocks/categories/all.html',
        data,
        context_instance=RequestContext(request),
    )
