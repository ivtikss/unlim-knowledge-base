from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


def user_avatar_path(instance):
    return f'avatars/user_{instance.user.id}/avatar'


class TypeStatus(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип статуса'
        verbose_name_plural = 'Типы статусов'
        ordering = ['name']


class TypeProduct(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'
        ordering = ['name']


class TypeCertification(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип сертификации'
        verbose_name_plural = 'Типы сертификации'
        ordering = ['name']


class TypeLicense(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип лицензии'
        verbose_name_plural = 'Типы лицензий'
        ordering = ['name']


class TypeGet(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип отгрузки'
        verbose_name_plural = 'Типы отгрузки'
        ordering = ['name']


class TypeReliase(models.Model):
    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип реализации'
        verbose_name_plural = 'Типы реализации'
        ordering = ['name']


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatar_path',
                               null=True,
                               blank=True)


class Vendor(models.Model):
    name = models.CharField(max_length=50,
                            default='',
                            null=True,
                            verbose_name='Наименование',
                            db_index=True)

    status = models.CharField(max_length=50,
                              default='',
                              null=True,
                              verbose_name='Статус',
                              blank=True)

    date = models.DateField(verbose_name='Срок действия партнерского статуса',
                            blank=True,
                            null=True)

    requirement = models.CharField(max_length=50,
                                   default='', null=True,
                                   verbose_name='Требования к партнерскому '
                                                'статусу',
                                   blank=True)

    discount = models.CharField(max_length=50,
                                default='',
                                null=True,
                                verbose_name='Скидка',
                                blank=True)

    def get_absolute_url(self):
        return reverse('vendor-detail',
                       kwargs={"vendor_id": self.pk})

    def get_edit_url(self):
        return reverse('edit-vendor',
                       kwargs={"vendor_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вендор'
        verbose_name_plural = 'Вендоры'
        ordering = ['name']


class VendorSpecialist(models.Model):
    vendor = models.ForeignKey('Vendor',
                               on_delete=models.CASCADE,
                               verbose_name='У какого вендора?',
                               blank=True,
                               null=True)

    name = models.CharField(max_length=150,
                            default='',
                            null=True,
                            verbose_name='ФИО',
                            blank=True)

    date = models.DateField(default=timezone.now,
                            verbose_name='Срок действия сертификатов '
                                         'специалистов',
                            blank=True,
                            null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертифицированный специалист'
        verbose_name_plural = 'Сертифицированные специалисты'
        ordering = ['name']


class Contact(models.Model):
    vendor = models.ForeignKey('Vendor',
                               on_delete=models.CASCADE,
                               default='',
                               null=True,
                               blank=True,
                               verbose_name='Вендор')

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                default='',
                                null=True,
                                blank=True,
                                verbose_name='Продукт')

    name = models.CharField(max_length=50,
                            default='',
                            verbose_name='ФИО')

    phone_number = models.CharField(max_length=50,
                                    default='',
                                    verbose_name='Номер телефона')
    email = models.CharField(max_length=50,
                             default='',
                             verbose_name='Адрес электронной почты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'
        ordering = ['name']


class VendorPrices(models.Model):
    vendor = models.ForeignKey('Vendor',
                               on_delete=models.CASCADE,
                               default='',
                               null=True,
                               blank=True)

    file = models.FileField(default='',
                            verbose_name='Файл прайса',
                            null=True,
                            blank=True,
                            upload_to='vendor_price')

    date = models.DateField(default='',
                            verbose_name='Дата начала действия прайса',
                            blank=True,
                            null=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы'
        ordering = ['vendor']


class Product(models.Model):  # Первичная информация
    vendor = models.ForeignKey(Vendor,
                               on_delete=models.CASCADE,
                               default='',
                               null=True)
    name = models.CharField(max_length=50,
                            default='',
                            null=True)
    product_type = models.ForeignKey(TypeProduct,
                                     on_delete=models.CASCADE,
                                     default='',
                                     null=True)
    top_certified = models.BooleanField(default=False,
                                        null=True)
    analogs = models.CharField(max_length=50,
                               default='',
                               null=True)
    brif_description = models.TextField(max_length=150,
                                        default='',
                                        null=True)
    whom_and_what_for = models.TextField(max_length=150,
                                         default='',
                                         null=True)
    ship_kit = models.CharField(max_length=200,
                                default='',
                                null=True)
    tech_support = models.CharField(max_length=250,
                                    default='',
                                    null=True)
    owner_type = models.CharField(max_length=100,
                                  default='',
                                  null=True)
    competitions = models.FileField(default=None,
                                    null=True, upload_to='vendor_price')
    gen_form = models.FileField(default=None,
                                null=True)
    battle_card = models.FileField(default=None,
                                   null=True)
    extra_comments1 = models.TextField(default='',
                                       null=True)

    type_reliz = models.ForeignKey(TypeReliase,
                                   on_delete=models.CASCADE,
                                   default='',
                                   null=True)
    reliz_brif = models.CharField(max_length=200,
                                  default='',
                                  null=True)
    type_license = models.ForeignKey(TypeLicense,
                                     on_delete=models.CASCADE,
                                     default='',
                                     null=True)
    license_brif = models.CharField(max_length=200,
                                    default='',
                                    null=True)
    license_date = models.DateField(default=timezone.now,
                                    blank=True,
                                    null=True)
    type_get = models.ForeignKey(TypeGet,
                                 on_delete=models.CASCADE,
                                 default='',
                                 null=True)
    get_brif = models.CharField(max_length=200,
                                default='',
                                null=True)
    type_cert = models.ForeignKey(TypeCertification,
                                  on_delete=models.CASCADE,
                                  default='',
                                  null=True)
    cert_brif = models.CharField(max_length=200,
                                 default='',
                                 null=True)
    cert_date = models.DateField(default=timezone.now,
                                 blank=True,
                                 null=True)

    tz_descriptions = models.FileField(default=None,
                                       null=True)
    tz_44fzs = models.FileField(default=None,
                                null=True)
    tz_date = models.DateField(default=timezone.now,
                               blank=True,
                               null=True)
    pilot_quests = models.FileField(default=None,
                                    null=True)
    pilot_pmis = models.FileField(default=None,
                                  null=True)
    pilot_descriptions = models.TextField(max_length=500,
                                          default='',
                                          null=True)
    pilot_plans = models.FileField(default=None,
                                   null=True)
    pilot_diss = models.CharField(max_length=50,
                                  default='',
                                  null=True)
    reg_axofts = models.FileField(default=None,
                                  null=True)

    contact_price = models.CharField(max_length=50,
                                     default='',
                                     null=True)

    reg_quest_register_deals = models.FileField(default=None,
                                                null=True)
    reg_reward_schemes = models.TextField(max_length=50,
                                          default='',
                                          null=True)
    extra_comments2 = models.TextField(default='',
                                       null=True)

    brochures = models.FileField(default=None,
                                 null=True)

    presentation_products = models.FileField(default=None,
                                             null=True)
    webinars = models.CharField(max_length=50,
                                default='',
                                null=True)
    presentations = models.CharField(max_length=50,
                                     default='',
                                     null=True)
    partner_webinars = models.CharField(max_length=50,
                                        default='',
                                        null=True)

    fsb_certified = models.BooleanField(default=False,
                                        null=True)
    fsteck_certified = models.BooleanField(default=False,
                                           null=True)

    def get_absolute_url(self):
        return reverse('product-detail',
                       kwargs={"product_id": self.pk})
    
    def __str__(self):
            return self.name


class GroupFAQ(models.Model):
    name = models.CharField(max_length=100,
                            default='',
                            null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа вопросов'
        verbose_name_plural = 'Группы вопросов'
        ordering = ['name']


class QuestionFAQ(models.Model):
    group = models.ForeignKey(GroupFAQ,
                              on_delete=models.CASCADE,
                              default=0)

    name = models.CharField(max_length=100,
                            default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['name', 'group']


class Answer(models.Model):
    question = models.ForeignKey('QuestionFAQ',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    description = models.TextField(default='',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'
        ordering = ['question', 'description']
