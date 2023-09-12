from .models import *
from django.forms import ModelForm


class TypeStatusForm(ModelForm):
    class Meta:
        model = TypeStatus
        fields = ['name']


class TypeProductForm(ModelForm):
    class Meta:
        model = TypeProduct
        fields = ['name']


class TypeCertificationForm(ModelForm):
    class Meta:
        model = TypeCertification
        fields = ['name']


class TypeLicenseForm(ModelForm):
    class Meta:
        model = TypeLicense
        fields = ['name']


class TypeGetForm(ModelForm):
    class Meta:
        model = TypeGet
        fields = ['name']


class TypeReliaseForm(ModelForm):
    class Meta:
        model = TypeReliase
        fields = ['name']


class NewVendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['name']


class NewVendorSpecialistForm(ModelForm):
    class Meta:
        model = VendorSpecialist
        fields = ['name']
