from django.conf.urls.defaults import *
 
urlpatterns = patterns('customers.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
    url(r'^update/(?P<customer_id>\d+)/$', 'update', name='update'),
)
