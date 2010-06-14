from django.shortcuts import render_to_response
from django.template import RequestContext

from stocks.forms import CategoryForm


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
