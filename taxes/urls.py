from django.conf.urls.defaults import *
 
urlpatterns = patterns('taxes.views',
    url(r'^$', 'index', name='index'),
    url(r'create/$', 'create', name='create'),
    url(r'delete/$', 'delete', name='delete'),
    url(r'update/(?P<tax_id>\d+)/$', 'update', name='update'),
)
