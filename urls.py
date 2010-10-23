from django import template
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('home.urls', namespace='home'), name='home'),
    url(r'^', include('hub_users.urls', namespace='hub-users'), name='hub-users'),
    url(r'^companies/', include('companies.urls', namespace='companies'), name='companies'),
    url(r'^contacts/', include('contacts.urls', namespace='contacts'), name='contacts'),
    url(r'^customers/', include('customers.urls', namespace='customers'), name='customers'),
    url(r'^geography/', include('geography.urls', namespace='geography'), name='geography'),
    url(r'^quotations/', include('quotations.urls', namespace='quotations'), name='quotations'),
    url(r'^sales/', include('sales.urls', namespace='sales'), name='sales'),
    url(r'^stocks/', include('stocks.urls', namespace='stocks'), name='stocks'),
    url(r'^suppliers/', include('suppliers.urls', namespace='suppliers'), name='suppliers'),
    url(r'^warehouses/', include('warehouses.urls', namespace='warehouses'), name='warehouses'),
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
