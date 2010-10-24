from django.conf.urls.defaults import *

urlpatterns = patterns('fcds.views',
    url(r'^$', 'index', name='index'),
)
