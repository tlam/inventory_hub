from django.contrib import admin

from contacts.models import Email, Phone
from customers.models import Customer


class EmailInline(admin.TabularInline):
    model = Email


class PhoneInline(admin.TabularInline):
    model = Phone


class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        EmailInline, PhoneInline,
    ]

admin.site.register(Customer, CustomerAdmin)
