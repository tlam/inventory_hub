from django.conf.urls.defaults import *
 
urlpatterns = patterns('geography.views',
    url(r'^search-city/$', 'search_city', name='search-city'),
    url(r'^search-country/$', 'search_country', name='search-country'),
)

