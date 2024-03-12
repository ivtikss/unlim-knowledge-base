import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from django.conf import settings


@login_required
def change_user_role(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        roles = request.POST.getlist("role")
        # Обновите роли пользователя в базе данных
    return redirect('/staff')


@login_required
def personal_page(request):
    if request.method == 'POST':
        form = ChangeUserInfoForm(request.POST, instance=request.user)

        uploaded_avatar = request.FILES.get('avatar')
        print(uploaded_avatar)
        if form.is_valid():
            form.save()

            if uploaded_avatar:
                if not hasattr(request.user, 'userprofile'):
                    UserProfile.objects.create(user=request.user)
                    request.user.userprofile.avatar = uploaded_avatar
                    request.user.userprofile.save()
                else:
                    request.user.userprofile.avatar = uploaded_avatar
                    request.user.userprofile.save()

            return redirect('PersonalPage')

    else:
        form = ChangeUserInfoForm(instance=request.user)
    return render(request, 'PersonalPage.html', {'form': form})


def is_admin(user):
    return user.groups.filter(name='Администратор').exists()


def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
            label=("E-mail"),
            max_length=254,
            widget=forms.EmailInput(attrs={"autocomplete": "email", "class" : "form-control"}),
        )
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
    


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = CustomPasswordResetForm


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


@login_required
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
        vendor_id = Vendor.objects.filter(name=vendor_filter).values_list('id',
                                                                          flat=True).first()
        if vendor_id:
            filtered_products = filtered_products.filter(vendor=vendor_id)

    if product_filter:
        filtered_products = filtered_products.filter(name=product_filter)

    if type_filter:
        type_id = TypeProduct.objects.filter(name=type_filter).values_list('id',
                                                                          flat=True).first()
        if type_id:
            filtered_products = filtered_products.filter(product_type=type_id)


    if not vendor_filter and not product_filter and not type_filter:
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
    return render(request, 'index1.html', context)


@user_passes_test(is_admin, login_url='/')
def staff(request):
    users = User.objects.all().order_by('last_name', 'first_name', 'email')
    roles = Group.objects.all()

    if request.POST.get('addUser'):
        email = request.POST.get('email')
        password = "1234"  # Заданный пароль
        role = request.POST.get('roles')
        group = Group.objects.get(name=role)
        try:
            user = User.objects.create_user(username=email, email=email,
                                            password=password)
            group.user_set.add(user)
            messages.success(request, "Пользователь успешно создан.")
            return redirect('UsersRoles')
        except Exception as e:
            print(e)
            messages.error(request, str(e))

    if request.POST.get('changeRole'):
        user_id = request.POST.get("user_id")
        user = User.objects.filter(pk=user_id).get()
        roles = request.POST.getlist("role")
        if in_group(user, 'Администратор') and ('Администратор' not in roles):
            group = Group.objects.get(name='Администратор')
            group.user_set.remove(user)
        if in_group(user, 'Сотрудник') and ('Сотрудник' not in roles):
            group = Group.objects.get(name='Сотрудник')
            group.user_set.remove(user)
        if in_group(user, 'Сотрудник ОПиР') and ('Сотрудник ОПиР' not in roles):
            group = Group.objects.get(name='Сотрудник ОПиР')
            group.user_set.remove(user)
        if in_group(user, 'Сотрудник ОС') and ('Сотрудник ОС' not in roles):
            group = Group.objects.get(name='Сотрудник ОС')
            group.user_set.remove(user)
        if in_group(user, 'Сотрудник Коммерческого блока') and (
                'Сотрудник Коммерческого блока' not in roles):
            group = Group.objects.get(name='Сотрудник Коммерческого блока')
            group.user_set.remove(user)
        if not (in_group(user, 'Администратор')) and ('Администратор' in roles):
            group = Group.objects.get(name='Администратор')
            group.user_set.add(user)
        if not (in_group(user, 'Сотрудник')) and ('Сотрудник' in roles):
            group = Group.objects.get(name='Сотрудник')
            group.user_set.add(user)
        if not (in_group(user, 'Сотрудник ОПиР')) and (
                'Сотрудник ОПиР' in roles):
            group = Group.objects.get(name='Сотрудник ОПиР')
            group.user_set.add(user)
        if not (in_group(user, 'Сотрудник ОС')) and ('Сотрудник ОС' in roles):
            group = Group.objects.get(name='Сотрудник ОС')
            group.user_set.add(user)
        if not (in_group(user, 'Сотрудник Коммерческого блока')) and (
                'Сотрудник Коммерческого блока' in roles):
            group = Group.objects.get(name='Сотрудник Коммерческого блока')
            group.user_set.add(user)
        return redirect('UsersRoles')

    context = {
        'users': users,
        'roles': roles,
    }
    return render(request, 'UsersRoles.html', context)


def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    specialist = VendorSpecialist.objects.filter(vendor=vendor_id).get()
    contact = Contact.objects.filter(vendor=vendor_id).get()
    prices = VendorPrices.objects.filter(vendor=vendor_id)
    today = datetime.date.today()
    nearest_date_diff = None
    nearest_price = None
    count = 0
    act_price = []
    fut_price = []
    pas_price = []

    for price in prices:
        price_date = price.date
        date_diff = (price_date - today).days
        if (nearest_date_diff is None or date_diff >= nearest_date_diff) and date_diff <= 0:
            count +=1
            nearest_date_diff = date_diff
            nearest_price = price

    if count != 0:
        act_price.append(nearest_price)
        prices = prices.exclude(pk=act_price[0].pk)

    for price in prices:
        price_date = price.date
        date_diff = (price_date - today).days

        if date_diff < 0:
            pas_price.append(price)
        elif date_diff > 0:
            fut_price.append(price)

    if request.POST:
        if 'delete' in request.POST:
            vendor_id = request.POST.get('vendor_id')
            vendor = Vendor(pk=vendor_id)
            vendor.delete()
            return redirect('/')
        if 'add_price' in request.POST:
            vendor_id = request.POST.get('vendor_id')
            vendor = Vendor(pk=vendor_id)
            current_price = request.FILES.get('currentPrice')
            date = request.POST.get('Date')
            print(current_price)
            price = VendorPrices(
                file=current_price,
                vendor=vendor,
                date=date,
            )

            price = price.save()
            return redirect("/vendor/" + f'{vendor.id}')

    if specialist and contact:
        context = {
            'vendor': vendor,
            'specialist': specialist,
            'contact': contact,
            'act_prices': act_price,
            'fut_prices': fut_price,
            'pas_prices': pas_price,
            'today': today,
        }
    else:
        context = {
            'vendor': vendor,
            'specialist': [],
            'contact': contact,
            'act_prices': act_price,
            'fut_prices': fut_price,
            'pas_prices': pas_price,
            'today': today,
        }

    return render(request, 'vendor_details.html', context)


def new_vendor(request):
    if request.POST:
        name = request.POST.get('vendorName')
        status = request.POST.get('partnerStatus')
        date = request.POST.get('partnerStatusExpiration')
        requirement = request.POST.get('partnerRequirements')
        discount = request.POST.get('discount')
        specialists_name = request.POST.get('certifiedSpecialists')
        specialists_date = request.POST.get(
            'certifiedSpecialistsExpiration')
        contact_name = request.POST.get('contactName')
        contact_phone = request.POST.get('contactPhone')
        contact_email = request.POST.get('contactEmail')
        current_price = request.FILES.get('currentPrice')
        future_price = request.FILES.get('futurePrice')
        price_future_date = request.POST.get('priceEffectiveDate')

        vendor = Vendor(name=name)

        if status:
            vendor.status = status
        if date:
            vendor.date = date
        if requirement:
            vendor.requirement = requirement
        if discount:
            vendor.discount = discount

        vendor = vendor.save()
        vendor = Vendor.objects.filter(name=name)[0]

        specialist = VendorSpecialist(vendor=vendor)
        if specialists_name:
            specialist.name = specialists_name
        else:
            specialist.name = ''
        if specialists_date:
            specialist.date = specialists_date
        else:
            specialist.date = None
        specialist = specialist.save()

        contact = Contact(vendor=vendor)
        if contact_name:
            contact.name = contact_name
        else:
            contact.name = ''
        if contact_phone:
            contact.phone_number = contact_phone
        else:
            contact.phone_number = ''
        if contact_email:
            contact.email = contact_email
        else:
            contact.email = ''

        contact = contact.save()

        if current_price:
            price1 = VendorPrices(
                file=current_price,
                vendor=vendor,
                date=datetime.date.today(),
            )
            price1 = price1.save()

        if future_price and price_future_date:
            price2 = VendorPrices(
                file=future_price,
                vendor=vendor,
                date=price_future_date,
            )
            price2 = price2.save()

        return redirect("/vendor/" + f'{vendor.id}')
    return render(request, 'new_vendor.html')


def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    specialist = VendorSpecialist.objects.filter(vendor=vendor_id).get()
    contact = Contact.objects.filter(vendor=vendor_id).get()

    if request.POST:
        name = request.POST.get('vendorName')
        status = request.POST.get('partnerStatus')
        date = request.POST.get('partnerStatusExpiration')
        requirement = request.POST.get('partnerRequirements')
        discount = request.POST.get('discount')

        specialists_name = request.POST.get('certifiedSpecialists')
        specialists_date = request.POST.get(
            'certifiedSpecialistsExpiration')

        contact_name = request.POST.get('contactName')
        contact_phone = request.POST.get('contactPhone')
        contact_email = request.POST.get('contactEmail')

        if name:
            vendor.name = name
        if status:
            vendor.status = status
        if date:
            vendor.date = date
        if requirement:
            vendor.requirement = requirement
        if discount:
            vendor.discount = discount

        vendor.save()
        vendor = Vendor.objects.filter(pk=vendor_id)[0]

        if specialists_name:
            specialist.name = specialists_name
        if specialists_date:
            specialist.date = specialists_date
        specialist.save()

        if contact_name:
            contact.name = contact_name
        if contact_phone:
            contact.phone_number = contact_phone
        if contact_email:
            contact.email = contact_email
        contact.save()

        return redirect("/vendor/" + f'{vendor.id}')

    context = {
        'vendor': vendor,
        'specialist': specialist,
        'contact': contact,
    }
    return render(request, 'edit_vendor.html', context)


def new_product(request):
    guides_status = TypeStatus.objects.all()
    guides_type_product = TypeProduct.objects.all()
    guide_type_certification = TypeCertification.objects.all()
    guides_type_license = TypeLicense.objects.all()
    guide_type_get = TypeGet.objects.all()
    guide_type_reliase = TypeReliase.objects.all()
    vendors = Vendor.objects.all()
    products = Product.objects.all()

    if request.POST:
        name = request.POST.get('productName')
        product = Product(name=name)
        if request.POST.get('top') == 'on':
            top = True
            product.top_certified = top
        if request.POST.get('productVendor'):
            vendorproduct = Vendor.objects.get(
                pk=request.POST.get('productVendor'))
            product.vendor = vendorproduct
        if request.POST.get('productType'):
            typeproduct = TypeProduct.objects.get(
                pk=request.POST.get('productType'))
            product.product_type = typeproduct
        if request.POST.get('Analogs'):
            product.analogs = request.POST.get('Analogs')
        if request.POST.get('shortDescription'):
            product.brif_description = request.POST.get('shortDescription')
        if request.POST.get('forWhom'):
            product.whom_and_what_for = request.POST.get('forWhom')
        if request.POST.get('shipmentKit'):
            product.ship_kit = request.POST.get('shipmentKit')
        if request.POST.get('techSupport'):
            product.tech_support = request.POST.get('techSupport')
        if request.POST.get('ownershipPrinciple'):
            product.owner_type = request.POST.get('ownershipPrinciple')
        if request.FILES.get('Competitions'):
            product.competitions = request.FILES.get('Competitions')
        if request.FILES.get('Anketa'):
            product.gen_form = request.FILES.get('Anketa')
        if request.FILES.get('BattleCard'):
            product.battle_card = request.FILES.get('BattleCard')
        if request.POST.get('additionalComment'):
            product.extra_comments1 = request.POST.get('additionalComment')

        if request.POST.get('relizType'):
            type_reliz = TypeReliase.objects.get(pk=request.POST.get('relizType'))
            product.type_reliz = type_reliz
        if request.POST.get('reliz_rel'):
            product.reliz_brif = request.POST.get('reliz_rel')
        if request.POST.get('licenseType'):
            type_license = TypeLicense.objects.get(
                pk=request.POST.get('licenseType'))
            product.type_license = type_license
        if request.POST.get('descr_lic'):
            product.license_brif = request.POST.get('descr_lic')
        if request.POST.get('GetType'):
            type_get = TypeGet.objects.get(pk=request.POST.get('GetType'))
            product.type_get = type_get
        if request.POST.get('descr_get'):
            product.get_brif = request.POST.get('descr_get')
        if request.POST.get('srtType'):
            type_cert = TypeCertification.objects.get(
                pk=request.POST.get('srtType'))
            if request.POST.get('SertDate'):
                date = request.POST.get('SertDate')
                product.cert_date = date
            product.type_cert = type_cert
        if request.POST.get('SertDesc'):
            product.cert_brif = request.POST.get('SertDesc')
            if request.POST.get('SertDate'):
                date = request.POST.get('SertDate')
                product.cert_date = date

        if request.FILES.get('tech'):
            product.tz_descriptions = request.FILES.get('tech')
        if request.FILES.get('tech44'):
            product.tz_44fzs = request.FILES.get('tech44')
        if request.FILES.get('anketa_pilot'):
            product.pilot_quests = request.FILES.get('anketa_pilot')
        if request.FILES.get('pmi'):
            product.pilot_pmis = request.FILES.get('pmi')
        if request.POST.get('pilot_dis'):
            product.pilot_descriptions = request.POST.get('pilot_dis')
        if request.FILES.get('plan'):
            product.pilot_plans = request.FILES.get('plan')
        if request.POST.get('distr'):
            product.pilot_diss = request.POST.get('distr')
        if request.POST.get('extra2'):
            product.extra_comments2 = request.POST.get('extra2')
        if request.FILES.get('axoft'):
            product.reg_axofts = request.FILES.get('axoft')
        if request.POST.get('contacts'):
            product.contact_price = request.POST.get('contacts')
        if request.FILES.get('reg'):
            product.reg_quest_register_deals = request.FILES.get('reg')
        if request.POST.get('sheme'):
            product.reg_reward_schemes = request.POST.get('sheme')

        if request.FILES.get('broch'):
            product.brochures = request.FILES.get('broch')
        if request.FILES.get('present_prod'):
            product.presentation_products = request.FILES.get('present_prod')
        if request.POST.get('veb'):
            product.webinars = request.POST.get('veb')
        if request.POST.get('present'):
            product.presentations = request.POST.get('present')
        if request.POST.get('close_veb'):
            product.partner_webinars = request.POST.get('close_veb')

        product = product.save()
        product = Product.objects.filter(name=name,
                                         brif_description=
                                         request.POST.get('shortDescription'),
                                         )[0]

        return redirect("/product/" + f'{product.id}')

    context = {
        'guides_status': guides_status,
        'guides_type_product': guides_type_product,
        'guide_type_certification': guide_type_certification,
        'guides_type_license': guides_type_license,
        'guide_type_get': guide_type_get,
        'guide_type_reliase': guide_type_reliase,
        'vendors': vendors,
        'products': products,
    }

    return render(request, 'Product_create.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if 'delete' in request.POST:
        product_id = request.POST.get('product_id')
        product = Product(pk=product_id)
        product.delete()
        return redirect('/')

    # context = {
    #     'guides_status': guides_status,
    #     'guides_type_product': guides_type_product,
    #     'guide_type_certification': guide_type_certification,
    #     'guides_type_license': guides_type_license,
    #     'guide_type_get': guide_type_get,
    #     'guide_type_reliase': guide_type_reliase,
    #     'vendors': vendors,
    #     'products': products,

    # }

    return render(request, 'Product_details.html', context={'product': product})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'Product_edit.html', context)