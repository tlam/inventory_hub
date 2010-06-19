from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from geography.models import City, Country


def search_city(request):
    city = request.GET.get('term', '')
    cities = City.objects.filter(name__icontains=city)
    cities = cities.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(cities))
    return HttpResponse(data, mimetype="application/javascript")


def search_country(request):
    country = request.GET.get('term', '')
    countries = Country.objects.filter(name__icontains=country)
    countries = countries.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(countries))
    return HttpResponse(data, mimetype="application/javascript")
