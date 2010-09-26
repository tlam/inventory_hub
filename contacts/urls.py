from django.conf.urls.defaults import *
        
urlpatterns = patterns('contacts.views',
    url(r'^add/$', 'add', name='add'),
    url(r'^ajax-email/$', 'ajax_email', name='ajax-email'),
    url(r'^ajax-remove-email/$', 'ajax_remove_email', name='ajax-remove-email'),
)
