from .models import Guide_status, Guide_type_product, Guide_type_certification
from .models import Guide_type_license, Guide_type_get, Guide_type_reliase, Vendor
from django.forms import ModelForm, TextInput

class Guide_statusForm(ModelForm):
    class Meta:
        model = Guide_status
        fields = ['name']

class Guide_type_productForm(ModelForm):
    class Meta:
        model = Guide_type_product
        fields = ['name']

class Guide_type_certificationForm(ModelForm):
    class Meta:
        model = Guide_type_certification
        fields = ['name']
class Guide_type_licenseForm(ModelForm):
    class Meta:
        model = Guide_type_license
        fields = ['name']

class Guide_type_getForm(ModelForm):
    class Meta:
        model = Guide_type_get
        fields = ['name']

class Guide_type_reliaseForm(ModelForm):
    class Meta:
        model = Guide_type_reliase
        fields = ['name']

class New_VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['name']

