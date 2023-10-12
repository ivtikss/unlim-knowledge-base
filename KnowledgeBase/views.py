from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


@login_required
def personal_page(request):
    if request.method == 'POST':
        form = ChangeUserInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('PersonalPage')  # Перенаправьте пользователя на страницу после изменения данных

    else:
        form = ChangeUserInfoForm(instance=request.user)

    return render(request, 'PersonalPage.html', {'form': form})


def is_admin(user):
    return user.groups.filter(name='Администратор').exists()


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


def user_logout(request):
    logout(request)
    return redirect('/login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/login.html', context)


@login_required
def guides(request):
    form = TypeStatusForm()
    guides_status = TypeStatus.objects.all()
    guides_type_product = TypeProduct.objects.all()
    guide_type_certification = TypeCertification.objects.all()
    guides_type_license = TypeLicense.objects.all()
    guide_type_get = TypeGet.objects.all()
    guide_type_reliase = TypeReliase.objects.all()

    if request.method == 'POST':
        if 'add_status' in request.POST:
            form = TypeStatusForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'add_product' in request.POST:
            form = TypeProductForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'add_certification' in request.POST:
            form = TypeCertificationForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'add_license' in request.POST:
            form = TypeLicenseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'add_get' in request.POST:
            form = TypeGetForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'add_reliase' in request.POST:
            form = TypeReliaseForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse(guides))
        if 'del_status' in request.POST:
            a = TypeStatus.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if 'del_product' in request.POST:
            a = TypeProduct.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if 'del_certification' in request.POST:
            a = TypeCertification.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if 'del_license' in request.POST:
            a = TypeLicense.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if 'del_get' in request.POST:
            a = TypeGet.objects.get(id=request.POST.get('id'))
            a.delete()
            return HttpResponseRedirect(reverse(guides))
        if 'del_reliase' in request.POST:
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
    guides_type_product = TypeProduct.objects.all()

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

    vendor_filter = request.GET.get('vendor')
    product_filter = request.GET.get('product')
    type_filter = request.GET.get('type')

    fstek_filter = request.GET.get('FSTEK')
    fsb_filter = request.GET.get('FSB')
    top_filter = request.GET.get('TOP')

    filtered_products = product

    if vendor_filter:
        vendor_id = Vendor.objects.filter(name=vendor_filter).values_list('id', flat=True).first()
        if vendor_id:
            filtered_products = filtered_products.filter(vendor=vendor_id)

    if product_filter:
        filtered_products = filtered_products.filter(name=product_filter)

    # if type_filter:
    #     filtered_products = filtered_products.filter(type__name=type_filter)

    if not vendor_filter and not product_filter:
        # Если нет параметров фильтрации, показываем все продукты
        filtered_products = product

    if fstek_filter:
        filtered_products = filtered_products.filter(fsteck_certified=True)

    if fsb_filter:
        filtered_products = filtered_products.filter(fsb_certified=True)

    if top_filter:
        filtered_products = filtered_products.filter(top_certified=True)

    context = {
        'vendors': vendor,
        'products': filtered_products,
        'group': group,
        'question': question,
        'answer': answer,
        'groupform': groupform,
        'questionform': questionform,
        'addanswerform': addanswerform,
        'all_type_product': guides_type_product,
    }
    return render(request, 'index.html', context)


@user_passes_test(is_admin, login_url='/')
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
