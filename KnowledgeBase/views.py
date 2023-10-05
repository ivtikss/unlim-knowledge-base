from django.contrib.auth.models import Group, User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib import messages


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


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
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('add_reliase'):
            form = TypeReliaseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_status'):
            a = TypeStatus.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_product'):
            a = TypeProduct.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_certification'):
            a = TypeCertification.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_license'):
            a = TypeLicense.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_get'):
            a = TypeGet.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if request.POST.get('del_reliase'):
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
    groupform = NewGroupFAQForm()
    questionform = NewQuestionFAQForm()
    addanswerform = NewAnswerForm()

    vendor = Vendor.objects.all()
    product = Product.objects.all()
    group = GroupFAQ.objects.all()
    question = QuestionFAQ.objects.all()
    answer = Answer.objects.all()

    if request.POST.get('add_group'):
        form = NewGroupFAQForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse(index))
    if request.POST.get('add_question'):
        form = NewQuestionFAQForm(request.POST)
        form = form.save(commit=False)
        form.group = GroupFAQ.objects.get(id=request.POST.get('group_id'))
        form.save()
        return HttpResponseRedirect(reverse(index))
    if request.POST.get('del_group'):
        a = GroupFAQ.objects.get(id=request.POST.get('group_id'))
        a.delete()
        return HttpResponseRedirect(reverse(index))
    if request.POST.get('del_quest'):
        a = QuestionFAQ.objects.get(id=request.POST.get('quest_id'))
        a.delete()
        return HttpResponseRedirect(reverse(index))
    if request.POST.get('add_answer'):
        form = NewAnswerForm(request.POST)
        a = form.save(commit=False)
        a.question = QuestionFAQ.objects.get(id=request.POST.get('quest_id'))
        a.save()
        return HttpResponseRedirect(reverse(index))
    if request.POST.get('edit_answer'):
        form = NewAnswerForm(request.POST)
        answer = Answer.objects.get(id=request.POST.get('answ_id'))
        form = form.save(commit=False)
        answer.description = form.description
        answer.save()
        return HttpResponseRedirect(reverse(index))

    form = NewGroupFAQForm()

    context = {
        'vendors': vendor,
        'products': product,
        'group': group,
        'question': question,
        'answer': answer,
        'groupform': groupform,
        'questionform': questionform,
        'addanswerform': addanswerform,
    }
    return render(request, 'index.html', context)


def staff(request):
    users = User.objects.all()
    roles = Group.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = "1234"  # Заданный пароль
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, "Пользователь успешно создан.")
            return redirect('UsersRoles')
        except Exception as e:
            print(e)
            messages.error(request, str(e))

    context = {
        'users': users,
        'roles': roles,
    }
    return render(request, 'UsersRoles.html', context)


def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    specialist = VendorSpecialist.objects.filter(vendor=vendor_id)
    contact = Contact.objects.filter(vendor=vendor_id)

    context = {
        'vendor': vendor,
        'specialist': specialist,
        'contact': contact,
    }

    return render(request, 'vendor_details.html', context)


def new_vendor(request):
    if request.POST:
        vendor = NewVendorForm(request.POST)
        vendor = vendor.save()

        vendorspecialist = NewVendorSpecialistForm(request.POST)
        vendorspecialist = vendorspecialist.save(commit=False)
        vendorspecialist.vendor = vendor
        vendorspecialist.save()

        return redirect(vendor)

    vendor = NewVendorForm()
    vendorspecialist = NewVendorSpecialistForm()

    context = {
        'vendor': vendor,
        'vendorspecialist': vendorspecialist
    }

    return render(request, 'new_vendor.html', context)


def new_product(request):
    return render(request, 'ProductCreate.html')
