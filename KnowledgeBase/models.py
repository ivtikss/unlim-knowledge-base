from django.db import models
from django.urls import reverse
import datetime
import django.utils


# Все модели сделать как модель Вендора, то есть добавить str, meta, verbose-name


class Vendor(models.Model):  # добавить поле дата
    name = models.CharField(max_length=50, default='', null=True, verbose_name='Наименование', db_index=True)
    logo = models.ImageField(default=None, null=True, verbose_name='Логотип')
    status = models.CharField(max_length=50, default='', null=True, verbose_name='Статус')
    requirement = models.CharField(max_length=50, default='', null=True, verbose_name='Требования к партнерскому '
                                                                                      'статусу')
    discount = models.CharField(max_length=50, default='', null=True, verbose_name='Скидка')

    def get_absolute_url(self):
        return reverse('vendor-detail', kwargs={"vendor_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вендор'
        verbose_name_plural = 'Вендоры'
        ordering = ['name']


class VendorSpecialist(models.Model):  # добавить дату и файл
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, verbose_name='У какого вендора?')
    name = models.CharField(max_length=50, default='', null=True, verbose_name='ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертифицированный специалист'
        verbose_name_plural = 'Сертифицированные специалисты'
        ordering = ['name']


class Contact(models.Model):  # добавить дату
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_DEFAULT, default='', null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_DEFAULT, default='', null=True)
    name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    messanger = models.CharField(max_length=20, default='')


class VendorPrices(models.Model):  # добавить дату
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    price = models.FileField(default=None)
    file = models.FileField(default=None)


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_DEFAULT, default='', null=True)
    name = models.CharField(max_length=50, default='', null=True)
    top = models.BooleanField(max_length=50, default=False, null=True)
    brif_description = models.TextField(default='', null=True)
    whom_and_what_for = models.TextField(default='', null=True)
    gen_form = models.FileField(default=None, null=True)
    ship_kit = models.CharField(max_length=200, default='', null=True)
    tech_support = models.CharField(max_length=200, default='', null=True)
    owner_type = models.CharField(max_length=100, default='', null=True)
    battle_card = models.FileField(default=None, null=True)
    product_type = models.CharField(max_length=50, default='', null=True)  # мб нужна связь с типами продукта
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


class TypeStatus(models.Model):
    name = models.CharField(max_length=100, default='')


class TypeProduct(models.Model):
    name = models.CharField(max_length=100, default='')


class TypeCertification(models.Model):
    name = models.CharField(max_length=100, default='')


class TypeLicense(models.Model):
    name = models.CharField(max_length=100, default='')


class TypeGet(models.Model):
    name = models.CharField(max_length=100, default='')


class TypeReliase(models.Model):
    name = models.CharField(max_length=100, default='')
