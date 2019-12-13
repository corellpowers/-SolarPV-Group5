from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #df
    path('', views.index, name='index'),
    #/aboutus/
    path('aboutus/', views.aboutus, name='aboutus'),
    #/registration/
    path('register/', views.register, name='register'),
    path('portal/', views.portal, name='portal'),
    path('portal/client/', views.client, name='client'),
    path('portal/location/', views.location, name='location'),
    path('portal/product/', views.product, name='product'),
    path('portal/teststandard/', views.teststandard, name='teststandard'),
    path('portal/certificate/', views.certificate, name='certificate'),
    path('portal/login/', views.login, name='login'),

]