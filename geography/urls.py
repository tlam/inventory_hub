from django.conf.urls.defaults import *
 
urlpatterns = patterns('geography.views',
    url(r'^add-country-ajax/$', 'add_country_ajax', name='add-country-ajax'),
    url(r'^add-town-ajax/$', 'add_town_ajax', name='add-town-ajax'),
    url(r'^search-city/$', 'search_city', name='search-city'),
    url(r'^search-country/$', 'search_country', name='search-country'),
)

