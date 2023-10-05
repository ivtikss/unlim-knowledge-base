from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='E-mail')
    password = forms.CharField(label='Пароль')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TypeStatusForm(forms.ModelForm):
    class Meta:
        model = TypeStatus
        fields = ['name']


class TypeProductForm(forms.ModelForm):
    class Meta:
        model = TypeProduct
        fields = ['name']
        widgets = {
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
        fields = ['name', 'status', 'date', 'requirement', 'discount']
        widgets = {
            'requirement': forms.Textarea(attrs={'row': 5})
        }

    prefix = 'vendor'


class NewVendorSpecialistForm(forms.ModelForm):
    class Meta:
        model = VendorSpecialist
        fields = ['name', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd.mm.YYYY (DOB)', 'class': 'PartnerSertificatedMenuinput'})
        }

    prefix = 'vendorspecialist'


class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'messanger']
        widgets = {

        }

    prefix = 'contact'


class NewVendorPricesForm(forms.ModelForm):
    class Meta:
        model = VendorPrices
        fields = ['vendor', 'file', 'date']
        widgets = {

        }

    prefix = 'price'


class NewGroupFAQForm(forms.ModelForm):
    class Meta:
        model = GroupFAQ
        fields = ['name']


class NewQuestionFAQForm(forms.ModelForm):
    class Meta:
        model = QuestionFAQ
        fields = ['name']


class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description', 'question']

    prefix = 'answer'
