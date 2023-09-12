from django.contrib import admin
from .models import *
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'status', 'discount', 'requirement')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'requirement')


admin.site.register(Vendor, VendorAdmin)


class VendorSpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor')
    list_display_links = ('id', 'name', 'vendor')
    search_fields = ('name', 'vendor')


admin.site.register(VendorSpecialist, VendorSpecialistAdmin)



