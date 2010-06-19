from django.conf.urls.defaults import *
 
urlpatterns = patterns('suppliers.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
)

