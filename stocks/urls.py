from django.conf.urls.defaults import *
 
urlpatterns = patterns('stocks.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
    url(r'^search-category/$', 'search_category', name='search-category'),
    url(r'^update/$', 'update', name='update'),
    url(r'^categories/', include('stocks.categories_urls', namespace='categories'), name='categories'),
)

