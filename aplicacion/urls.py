from django.contrib import admin
from django.urls import path
from aplicacion import views


urlpatterns = [
    path('', views.index),
    path('home/', views.login),
    path('perfil/', views.perfil),
    path('', views.updatePerfil),
    path('editPerfil/<id>', views.editPerfil),
    path('elimPerfil/', views.elimPerfil),
    path('logout/', views.logout_request, name= "logout"),
    path('perfil/', views.perfil, name="perfil"),
    path('RegistroUsuarios/', views.RegistroUsuarios),
    path('about/', views.about),
   

]
