
from django.contrib import admin
from django.urls import path
from kotlinApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservices/', views.myservices, name='myservices'),
    path('appointments/', views.appointment, name='appointments'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete ),
    path('edit/<int:id>', views.edit, name='edit' ),
    path('update/<int:id>', views.update, name='update' ),
    path('', views.register, name='register' ),
    path('login/', views.login, name='login' ),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]