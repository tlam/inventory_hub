from django.conf.urls.defaults import *
 
urlpatterns = patterns('warehouses.views',
    url(r'add-ajax/$', 'add_ajax', name='add-ajax'),
)
