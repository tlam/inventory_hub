from django.shortcuts import render_to_response
from django.template import RequestContext

from utils.tools import capwords
from warehouses.models import Warehouse


def add_ajax(request):
    new_warehouse = request.POST.get('new_warehouse', '')
    new_warehouse = capwords(new_warehouse)
    if new_warehouse:
        Warehouse.objects.get_or_create(name=new_warehouse)

    data = {
        'new_warehouse': new_warehouse,
        'warehouses': Warehouse.objects.order_by('name'),
    }

    return render_to_response(
        'warehouses/all.html',
        data,
        context_instance=RequestContext(request),
    )
