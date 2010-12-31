from django.conf.urls.defaults import *
 
urlpatterns = patterns('stocks.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/$', 'create', name='create'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^search-category/$', 'search_category', name='search-category'),
    url(r'^search-stock/(?P<category_id>\d+)/$', 'search_stock', name='search-stock'),
    url(r'^update/(?P<stock_id>\d+)/$', 'update', name='update'),
    url(r'^categories/', include('stocks.categories_urls', namespace='categories'), name='categories'),
    url(r'^colours/add-ajax/', 'add_colour_ajax', name='add-colour-ajax'),
)

