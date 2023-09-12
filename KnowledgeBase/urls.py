from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', index, name='index'),
    path('vendor/<int:pk>/', vendor_detail, name='vendor-detail'),
    path('guides/', guides, name='Guide'),
    path('staff/', staff, name='UsersRoles'),
    path('lk/', TemplateView.as_view(template_name='PersonalPage.html'), name='PersonalPage'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('new_vendor/', new_vendor, name='new_vendor'),
]
