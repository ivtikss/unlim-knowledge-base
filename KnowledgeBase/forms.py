from .models import *
from django import forms


class TypeStatusForm(forms.ModelForm):
    class Meta:
        model = TypeStatus
        fields = ['name']


class TypeProductForm(forms.ModelForm):
    class Meta:
        model = TypeProduct
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'PartnersName'})
        }


class TypeCertificationForm(forms.ModelForm):
    class Meta:
        model = TypeCertification
        fields = ['name']


class TypeLicenseForm(forms.ModelForm):
    class Meta:
        model = TypeLicense
        fields = ['name']


class TypeGetForm(forms.ModelForm):
    class Meta:
        model = TypeGet
        fields = ['name']


class TypeReliaseForm(forms.ModelForm):
    class Meta:
        model = TypeReliase
        fields = ['name']


class NewVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'status', 'requirement', 'discount']
        widgets = {
            'requirement': forms.Textarea(attrs={'row': 5})
        }

    prefix = 'vendor'


class NewVendorSpecialistForm(forms.ModelForm):
    class Meta:
        model = VendorSpecialist
        fields = ['name', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd.mm.YYYY (DOB)', 'class': 'form-control'})
        }

    prefix = 'vendorspecialist'
