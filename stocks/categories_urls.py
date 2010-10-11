from django.conf.urls.defaults import *

urlpatterns = patterns('stocks.categories_views',
    url(r'^$', 'index', name='index'),
    url(r'^add-ajax/$', 'add_ajax', name='add-ajax'),
    url(r'^create/$', 'create', name='create'),
    url(r'^update/(?P<category_id>\d+)/$', 'update', name='update'),
)
