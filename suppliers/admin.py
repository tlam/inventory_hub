from django.contrib import admin

from suppliers.models import ForeignSupplier, LocalSupplier

admin.site.register(ForeignSupplier)
admin.site.register(LocalSupplier)
