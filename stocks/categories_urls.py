from django.conf.urls.defaults import *

urlpatterns = patterns('stocks.categories_views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
    url(r'^update/$', 'update', name='update'),
)
