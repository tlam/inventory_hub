from django.conf.urls.defaults import *

urlpatterns = patterns('customers.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
    url(r'^customer-number-ajax/$', 'customer_number_ajax', \
        name='customer-number-ajax'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^update/(?P<customer_id>\d+)/$', 'update', name='update'),
)
