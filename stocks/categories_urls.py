from django.conf.urls.defaults import *

urlpatterns = patterns('stocks.categories_views',
    url(r'^$', 'index', name='index'),
    url(r'^add-ajax/$', 'add_ajax', name='add-ajax'),
    url(r'^create/$', 'create', name='create'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^inventory/(?P<category_id>\d+)/$', 'inventory', name='inventory'),
    url(r'^update/(?P<category_id>\d+)/$', 'update', name='update'),
)
