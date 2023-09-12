from .models import *
from django.contrib.auth.models import Group, User
from django.utils.functional import *
from django.urls import reverse_lazy, reverse
from .forms import Guide_statusForm, Guide_type_productForm, Guide_type_certificationForm
from .forms import Guide_type_licenseForm, Guide_type_getForm, Guide_type_reliaseForm, New_VendorForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
import time

def guides(request):
    form = Guide_statusForm()

    guides_status = Guide_status.objects.all()
    guides_type_product = Guide_type_product.objects.all()
    guide_type_certification = Guide_type_certification.objects.all()
    guides_type_license = Guide_type_license.objects.all()
    guide_type_get = Guide_type_get.objects.all()
    guide_type_reliase = Guide_type_reliase.objects.all()

    if (request.method == 'POST'):
        if request.POST.get('add_status'):
            form = Guide_statusForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_product'):
            form = Guide_type_productForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_certification'):
            form = Guide_type_certificationForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_license'):
            form = Guide_type_licenseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_get'):
            form = Guide_type_getForm(request.POST)
            print(form)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_reliase'):
            form = Guide_type_reliaseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_status'):
            print(request.POST.get('del_status'))
            a = Guide_status.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_product'):
            print(request.POST.get('del_product'))
            a = Guide_type_product.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_certification'):
            print(request.POST.get('del_certification'))
            a = Guide_type_certification.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_license'):
            print(request.POST.get('del_license'))
            a = Guide_type_license.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_get'):
            print(request.POST.get('del_get'))
            a = Guide_type_get.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_reliase'):
            print(request.POST.get('del_reliase'))
            a = Guide_type_reliase.objects.get(id = request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))

        
    
    form = Guide_statusForm()

    context = {
        'all_type_product' : guides_type_product,
        'all_type_certification' : guide_type_certification,
        'all_type_license' : guides_type_license,
        'all_type_get' : guide_type_get,
        'all_type_reliase' : guide_type_reliase,
        'all_status' : guides_status, 
        'form' : form,
    }
    return render(request, 'Guide.html', context)

def index(request):
    vendor = Vendor.objects.all()
    product = Product.objects.all()
    group = GroupFAQ.objects.all()
    question = QuestionFAQ.objects.all()
    answer = Answer.objects.all()
    print(answer)

    context = {
        'vendors' : vendor,
        'products' : product,
        'group' : group, 
        'question' : question,
        'answer' : answer,
    }
    return render(request, 'index.html', context)

def staff(request):
    users = User.objects.all()
    roles = Group.objects.all()

    context = {
        'users' : users,
        'roles' : roles,
    }
    return render(request, 'UsersRoles.html', context)

def vendor_detail(request, pk):
    context = {}

    vendor = Vendor.objects.get(id=pk)
    specialist = VendorSpecialist.objects.filter(vendor = pk)
    contact = Contact.objects.filter(vendor = pk)

    context = {
        'vendor': vendor,
        'specialist' : specialist,
        'contact' : contact, 
    }

    return render(request, 'vendor_details.html', context)

def new_vendor(request):
    context = {}
    a = None
    vendor = New_VendorForm()
    if request.POST.get('add_vendor'):
        vendor = New_VendorForm(request.POST)
        vendor.save()
        return HttpResponseRedirect(reverse(index))
    
    vendor = New_VendorForm()

    context = {
        'vendor' : vendor,
        'a' : a,
    }

    return render(request, 'new_vendor.html', context)