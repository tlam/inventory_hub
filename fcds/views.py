from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from stocks.models import Category


def index(request):
    data = {
        'categories': Category.objects.all(),
    }

    return render_to_response(
        'fcds/index.html',
        data,
        context_instance=RequestContext(request),
    )
