from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',
         index,
         name='index'),

    path('vendor/<int:vendor_id>/',
         vendor_detail,
         name='vendor-detail'),

    path('vendor/edit/<int:vendor_id>/',
         edit_vendor,
         name='edit-vendor'),

    path('new_vendor/',
         new_vendor,
         name='new_vendor'),

    path('guides/',
         guides,
         name='Guide'),

    path('staff/',
         staff,
         name='UsersRoles'),

    path('lk/',
         personal_page,
         name='PersonalPage'),

    path('logout/',
         user_logout,
         name='logout'),

    path('new_product/',
         new_product,
         name='new_product'),

    path('product/edit/<int:product_id>/',
         edit_product,
         name='edit-product'),

    path('product/<int:product_id>/',
         product_detail,
         name='product-detail'),

    path('login/',
         user_login,
         name='user_login'),

    path('auth/login/',
         lambda request: redirect('/login/')),

    path('reset_password/',
         UserPasswordResetView.as_view(),
         name='user_password_reset'),

    path('auth/password_reset/',
         lambda request: redirect('/reset_password/')),

    path('reset_password/done/',
         UserPasswordResetDoneView.as_view(),
         name='user_password_reset_done'),

    path('auth/password_reset/done/',
         lambda request: redirect('/reset_password/done/')),

    path('auth/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
         name='user_password_reset_confirm'),

    path('auth/reset/done/',
         UserPasswordResetDoneView.as_view(
             template_name='registration/password_change_done.html'),
         name='user_password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
