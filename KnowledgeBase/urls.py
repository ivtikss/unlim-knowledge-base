from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('vendor/<int:vendor_id>/', vendor_detail, name='vendor-detail'),
    path('new_vendor/', new_vendor, name='new_vendor'),
    path('guides/', guides, name='Guide'),
    path('staff/', staff, name='UsersRoles'),
    path('lk/', TemplateView.as_view(template_name='PersonalPage.html'), name='PersonalPage'),
    path('logout/', user_logout, name='user_logout'),
    path('new_product/', new_product, name='create_product'),
    path('login/', user_login, name='user_login'),
    path('accounts/login/', user_login, name='user_login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
