from django.conf.urls.defaults import *
 
urlpatterns = patterns('sales.views',
    url(r'^$', 'index', name='index'),
    url(r'(?P<sale_type>(cash|credit))/customer/$', 'customer', name='customer'),
    url(r'(?P<sale_type>(cash|credit))/delete/$', 'delete', name='delete'),
    url(r'(?P<sale_type>(cash|credit))/create/(?P<customer_id>\d+)/$', 'create', name='create'),
    url(r'(?P<sale_type>(cash|credit))/update/(?P<sale_id>\d+)/$', 'update', name='update'),
)
