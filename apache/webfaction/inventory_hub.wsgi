import os
import sys

sys.path = ['/home/tlam/webapps/inventory_hub', '/home/tlam/webapps/inventory_hub/inventory_hub/', '/home/tlam/webapps/inventory_hub/lib/python2.6'] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_hub.settings'
application = WSGIHandler()
