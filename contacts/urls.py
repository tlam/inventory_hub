from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',
    url(r'^ajax-add-email/$', 'ajax_add_email', name='ajax-add-email'),
    url(r'^ajax-remove-email/$', 'ajax_remove_email', \
        name='ajax-remove-email'),
)
