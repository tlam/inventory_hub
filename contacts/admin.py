from django.contrib import admin

from contacts.models import Contact, ContactList, Email, Phone


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    inlines = [
        EmailInline,
        PhoneInline,
    ]


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class ContactListAdmin(admin.ModelAdmin):
    inlines = [
        ContactInline,
    ]


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactList, ContactListAdmin)
admin.site.register(Email)
admin.site.register(Phone)
