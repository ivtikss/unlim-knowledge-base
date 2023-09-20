from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(TypeStatus)
admin.site.register(TypeProduct)
admin.site.register(TypeCertification)
admin.site.register(TypeLicense)
admin.site.register(TypeGet)
admin.site.register(TypeReliase)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'date', 'discount', 'requirement')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'requirement')


admin.site.register(Vendor, VendorAdmin)


class VendorSpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'vendor')


admin.site.register(VendorSpecialist, VendorSpecialistAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'product', 'phone_number', 'email', 'messanger')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'vendor', 'name')


admin.site.register(Contact, ContactAdmin)


class VendorPricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'file', 'date')
    list_display_links = ('id', 'file')
    search_fields = ('vendor', 'date')


admin.site.register(VendorPrices, VendorPricesAdmin)

