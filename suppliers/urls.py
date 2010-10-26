from django.conf.urls.defaults import *
 
urlpatterns = patterns('suppliers.views',
    url(r'^$', 'base_index', name='index'),
    url(r'^foreign/create/$', 'create_foreign', name='create-foreign'),
    url(r'^foreign/update/(?P<supplier_id>\d+)/$', 'update_foreign', name='update-foreign'),
    url(r'^local/create/$', 'create_local', name='create-local'),
    url(r'^local/update/(?P<supplier_id>\d+)/$', 'update_local', name='update-local'),
    url(r'(?P<supplier_type>(foreign|local))/$', 'index', name='index'),
    url(r'(?P<supplier_type>(foreign|local))/delete/$', 'delete', name='delete'),
    url(r'(?P<supplier_type>(foreign|local))/supplier-number-ajax/$', 'supplier_number_ajax', name='supplier-number-ajax'),
)

