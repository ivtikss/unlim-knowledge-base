from django.db import models
import datetime
import django.utils



class Vendor(models.Model):
    name = models.CharField(max_length=50, default='', null=True)
    logo = models.ImageField(default=None, null=True)
    status = models.CharField(max_length=50, default='', null=True)
    period = models.DateField(max_length=50, default=django.utils.timezone.now,null=True)
    requirement = models.CharField(max_length=50, default='', null=True)
    discount =  models.CharField(max_length=50, default='', null=True)

class VendorSpecialist(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', null=True)
    date = models.DateField(max_length=50, default=django.utils.timezone.now, null=True)
    file = models.FileField(null=True)

class Contact(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_DEFAULT, default='', null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_DEFAULT, default='', null=True)
    name = models.CharField(max_length=50, default='')
    period = models.DateField(max_length=50, default=django.utils.timezone.now)
    phone_number = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    messanger = models.CharField(max_length=20, default='')
class VendorPrices(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    price = models.FileField(default=None)
    date = models.DateField(default=django.utils.timezone.now)
    file = models.FileField(default=None)



class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_DEFAULT, default='', null=True)
    name = models.CharField(max_length=50, default='', null=True)
    top = models.BooleanField(max_length=50, default=False, null=True)
    brif_description = models.TextField(default='', null=True)
    whom_and_what_for = models.TextField(default='',null=True)
    gen_form = models.FileField(default=None, null=True)
    ship_kit = models.CharField(max_length=200, default='', null=True)
    tech_support = models.CharField(max_length=200, default='', null=True)
    owner_type = models.CharField(max_length=100, default='', null=True)
    battle_card = models.FileField(default=None, null=True)
    product_type = models.CharField(max_length=50, default='', null=True) # мб нужна связь с типами продукта
    competencies = models.FileField(default=None, null=True)
    analogs = models.CharField(max_length=50, default='', null=True)

# class __Skeleton(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='', name='id Продукта')
#     name = models.CharField(max_length=50, default='')

#     class Meta:
#         abstract = True


# class Realisation(__Skeleton):
#     pass


# class Department(__Skeleton):
#     description = models.TextField(default='')


# class Licence(__Skeleton):
#     description = models.TextField(default='')
#     date = models.DateField(default=django.utils.timezone.now)


# class Price(__Skeleton):
#     description = models.TextField(default='')
#     file = models.FileField(default=None)


# class Certification(__Skeleton):
#     date = models.DateField(default=django.utils.timezone.now)
#     file = models.FileField(default=None)


# class InfoDeal(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')

#     # Техническое задание
#     tz_description = models.FileField(default=None)
#     tz_44fz = models.FileField(default=None)
#     tz_date = models.DateField(default=django.utils.timezone.now)


#     # Для проведения пилота
#     pilot_quest = models.FileField(default=None)
#     pilot_pmi = models.FileField(default=None)
#     pilot_path = models.CharField(max_length=50, default='')

#     #    Как проведения пилота
#     pilot_description = models.FileField(default=None)
#     pilot_plan = models.FileField(default=None)

#     # Для регистрации сделок
#     reg_axoft = models.FileField(default=None)
#     # контакты отдельно
#     reg_quest_register_deal = models.FileField(default=None)
#     reg_partnership_status = models.FileField(default=None)
#     reg_reward_scheme = models.TextField(max_length=50, default='')

#     extra_comment = models.TextField(default='')


# class ExtraInfo(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')
#     # Материалы для ознакомления от вендоров
#     brochure = models.FileField(default=None)
#     presentation_product = models.FileField(default=None)
#     webinar = models.CharField(max_length=50, default='')
#     # Внутренние материалы
#     presentation = models.CharField(max_length=50, default='')
#     partner_webinar = models.CharField(max_length=50, default='')

class GroupFAQ(models.Model):
    name = models.CharField(max_length=100, default='', null=False)


class QuestionFAQ(models.Model):
    group = models.ForeignKey(GroupFAQ, on_delete=models.SET_DEFAULT, default=0)
    name = models.CharField(max_length=100, default='')


class Answer(models.Model):
    question = models.ForeignKey('QuestionFAQ', on_delete=models.SET_DEFAULT, default=0)
    description = models.TextField(default='')
    files = models.FileField(default=None)

class Guide_status(models.Model):
    name = models.CharField(max_length=100, default='')

class Guide_type_product(models.Model):
    name = models.CharField(max_length=100, default='')

class Guide_type_certification(models.Model):
    name = models.CharField(max_length=100, default='')

class Guide_type_license(models.Model):
    name = models.CharField(max_length=100, default='')

class Guide_type_get(models.Model):
    name = models.CharField(max_length=100, default='')

class Guide_type_reliase(models.Model):
    name = models.CharField(max_length=100, default='')