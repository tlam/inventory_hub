from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',
    url(r'^add-contact/$', 'add_contact', name='add-contact'),
    url(r'^add-email/$', 'add_email', name='add-email'),
    url(r'^add-phone/$', 'add_phone', name='add-phone'),
    url(r'^ajax-remove-contact/$', 'ajax_remove_contact', \
        name='ajax-remove-contact'),
    url(r'^ajax-remove-email/$', 'ajax_remove_email', \
        name='ajax-remove-email'),
    url(r'^ajax-remove-phone/$', 'ajax_remove_phone', \
        name='ajax-remove-phone'),
)
