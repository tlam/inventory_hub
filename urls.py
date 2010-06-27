from django import template
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('home.urls', namespace='home'), name='home'),
    url(r'^', include('hub_users.urls', namespace='hub-users'), name='hub-users'),
    url(r'^customers/', include('customers.urls', namespace='customers'), name='customers'),
    url(r'^geography/', include('geography.urls', namespace='geography'), name='geography'),
    url(r'^sales/', include('sales.urls', namespace='sales'), name='sales'),
    url(r'^stocks/', include('stocks.urls', namespace='stocks'), name='stocks'),
    url(r'^suppliers/', include('suppliers.urls', namespace='suppliers'), name='suppliers'),
)

# Load custom template tags and filters in all templates
template.add_to_builtins('utils.templatetags.extras')

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
