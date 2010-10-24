from django.conf.urls.defaults import *
 
urlpatterns = patterns('suppliers.views',
    url(r'^$', 'index', name='index'),
    url(r'^delete/$', 'index_foreign', name='index-foreign'),
    url(r'^foreign/$', 'index_foreign', name='index-foreign'),
    url(r'^foreign/create/$', 'create_foreign', name='create-foreign'),
    url(r'^foreign/delete/$', 'delete_foreign', name='delete-foreign'),
    url(r'^foreign/update/(?P<supplier_id>\d+)/$', 'update_foreign', name='update-foreign'),
    url(r'^lcoal/$', 'index_local', name='index-local'),
    url(r'^local/create/$', 'create_local', name='create-local'),
    url(r'^local/delete/$', 'delete_local', name='delete-local'),
    url(r'^local/update/(?P<supplier_id>\d+)/$', 'update_local', name='update-local'),
    url(r'(?P<supplier_type>(foreign|local))/supplier-number-ajax/$', 'supplier_number_ajax', name='supplier-number-ajax'),
)

