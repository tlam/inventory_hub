from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from geography.models import City, Country, Town
from utils.tools import capwords


def add_country_ajax(request):
    new_country = request.POST.get('new_country', '')
    new_country = capwords(new_country)
    if new_country:
        Country.objects.get_or_create(name=new_country)

    data = {
        'countries': Country.objects.order_by('name'),
        'new_country': new_country,
    }

    return render_to_response(
        'geography/countries.html',
        data,
        context_instance=RequestContext(request),
    )


def add_town_ajax(request):
    new_town = request.POST.get('new_town', '')
    new_town = capwords(new_town)
    if new_town:
        Town.objects.get_or_create(name=new_town)

    data = {
        'towns': Town.objects.order_by('name'),
        'new_town': new_town,
    }

    return render_to_response(
        'geography/towns.html',
        data,
        context_instance=RequestContext(request),
    )


def search_city(request):
    """
    AJAX call to autocomplete city name
    """
    city = request.GET.get('term', '')
    cities = City.objects.filter(name__icontains=city)
    cities = cities.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(cities))
    return HttpResponse(data, mimetype="application/javascript")


def search_country(request):
    """
    AJAX call to autocomplete country name
    """
    country = request.GET.get('term', '')
    countries = Country.objects.filter(name__icontains=country)
    countries = countries.values_list('name', flat=True).order_by('name')
    data = simplejson.dumps(list(countries))
    return HttpResponse(data, mimetype="application/javascript")


