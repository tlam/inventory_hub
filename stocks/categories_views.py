from django.contrib import messages
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from stocks.forms import CategoryForm
from stocks.models import Category
from utils.tools import capwords


def index(request):
    categories = Category.objects.all()

    data = {
        'categories': categories,
    }

    return render_to_response(
        'stocks/categories/index.html',
        data,
        context_instance=RequestContext(request),
    )


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created')
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


def update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated')
    else:
        form = CategoryForm(instance=category)

    data = {
        'form': form,
    }

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
