from django.contrib import admin

from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone_no', 'language', 'currency']
    search_fields = ['user', 'name']


admin.site.register(Supplier, SupplierAdmin)

