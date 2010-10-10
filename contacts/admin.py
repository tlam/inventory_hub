from django.contrib import admin

from contacts.models import Email, Phone


admin.site.register(Email)
admin.site.register(Phone)
