import os
import sys

sys.path = ['/home/tlam/webapps/inventory_hub', '/home/tlam/webapps/inventory_hub/inventory_hub/', '/home/tlam/.virtualenvs/django/lib/python2.7'] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_hub.settings'
application = WSGIHandler()
