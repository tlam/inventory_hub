from django.conf.urls.defaults import *
 
urlpatterns = patterns('sales.views',
    url(r'^$', 'index', name='index'),
    url(r'(?P<sale_type>(cash|credit))/customer/$', 'customer', name='customer'),
    url(r'(?P<sale_type>(cash|credit))/create/(?P<customer_id>\d+)/$', 'create', name='create'),
    url(r'^cash/update/(?P<sale_id>\d+)/$', 'update_cash_sale', name='update-cash-sale'),
)
