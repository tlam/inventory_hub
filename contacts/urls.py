from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',
    #url(r'^ajax-add-email/$', 'ajax_add_email', name='ajax-add-email'),
    url(r'^add-contact/$', 'add_contact', name='add-contact'),
    url(r'^add-email/$', 'add_email', name='add-email'),
    url(r'^add-phone/$', 'add_phone', name='add-phone'),
    url(r'^ajax-add-phone/$', 'ajax_add_phone', name='ajax-add-phone'),
    url(r'^ajax-remove-email/$', 'ajax_remove_email', \
        name='ajax-remove-email'),
    url(r'^ajax-remove-phone/$', 'ajax_remove_phone', \
        name='ajax-remove-phone'),
)
