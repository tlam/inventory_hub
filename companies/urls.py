from django.conf.urls.defaults import *
 
urlpatterns = patterns('companies.views',
    url(r'^$', 'index', name='index'),
    url(r'create/$', 'create', name='create'),
    url(r'delete/$', 'delete', name='delete'),
    url(r'update/(?P<company_id>\d+)/$', 'update', name='update'),
)
