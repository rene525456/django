from django.urls import path

from . import views

urlpatterns=[
    path('', views.loginPage, name='autenticar'),
    path('logout', views.logoutPage, name='logout'),

]
