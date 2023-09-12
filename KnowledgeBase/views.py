from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *


def guides(request):
    form = TypeStatusForm()

    guides_status = TypeStatus.objects.all()
    guides_type_product = TypeProduct.objects.all()
    guide_type_certification = TypeCertification.objects.all()
    guides_type_license = TypeLicense.objects.all()
    guide_type_get = TypeGet.objects.all()
    guide_type_reliase = TypeReliase.objects.all()

    if request.method == 'POST':
        if request.POST.get('add_status'):
            form = TypeStatusForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_product'):
            form = TypeProductForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_certification'):
            form = TypeCertificationForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_license'):
            form = TypeLicenseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_get'):
            form = TypeGetForm(request.POST)
            print(form)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_reliase'):
            form = TypeReliaseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_status'):
            print(request.POST.get('del_status'))
            a = TypeStatus.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_product'):
            print(request.POST.get('del_product'))
            a = TypeProduct.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_certification'):
            print(request.POST.get('del_certification'))
            a = TypeCertification.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_license'):
            print(request.POST.get('del_license'))
            a = TypeLicense.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_get'):
            print(request.POST.get('del_get'))
            a = TypeGet.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_reliase'):
            print(request.POST.get('del_reliase'))
            a = TypeReliase.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))

    form = TypeStatusForm()

    context = {
        'all_type_product': guides_type_product,
        'all_type_certification': guide_type_certification,
        'all_type_license': guides_type_license,
        'all_type_get': guide_type_get,
        'all_type_reliase': guide_type_reliase,
        'all_status': guides_status,
        'form': form,
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
        'vendors': vendor,
        'products': product,
        'group': group,
        'question': question,
        'answer': answer,
    }
    return render(request, 'index.html', context)


def staff(request):
    users = User.objects.all()
    roles = Group.objects.all()

    context = {
        'users': users,
        'roles': roles,
    }
    return render(request, 'UsersRoles.html', context)


def vendor_detail(request, pk):

    vendor = Vendor.objects.get(id=pk)
    specialist = VendorSpecialist.objects.filter(vendor=pk)
    contact = Contact.objects.filter(vendor=pk)

    context = {
        'vendor': vendor,
        'specialist': specialist,
        'contact': contact,
    }

    return render(request, 'vendor_details.html', context)


def new_vendor(request):
    vendor = NewVendorForm()
    if request.POST.get('add_vendor'):
        vendor = NewVendorForm(request.POST)
        vendor.save()
        return HttpResponseRedirect(reverse(index))
    
    vendor = NewVendorForm()

    context = {
        'vendor': vendor,
    }

    return render(request, 'new_vendor.html', context)
