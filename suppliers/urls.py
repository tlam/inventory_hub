from django.conf.urls.defaults import *
 
urlpatterns = patterns('suppliers.views',
    url(r'^$', 'index', name='index'),
    url(r'^foreign/$', 'index_foreign', name='index-foreign'),
    url(r'^foreign/create/$', 'create_foreign', name='create-foreign'),
    url(r'^foreign/update/(?P<supplier_id>\d+)/$', 'update_foreign', name='update-foreign'),
)

