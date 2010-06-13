from django.conf.urls.defaults import *
 
urlpatterns = patterns('hub_users.views',
    url(r'^login/$', 'user_login', name='login'),
    url(r'^logout/$', 'user_logout', name='logout'),
)

