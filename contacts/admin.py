from django.contrib import admin

from contacts.models import Contact, ContactList, Email, Phone


admin.site.register(Contact)
admin.site.register(ContactList)
admin.site.register(Email)
admin.site.register(Phone)
