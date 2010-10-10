from django.contrib import admin

from contacts.models import Email
from customers.models import Customer


class EmailInline(admin.TabularInline):
    model = Email


class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        EmailInline,
    ]

admin.site.register(Customer, CustomerAdmin)
