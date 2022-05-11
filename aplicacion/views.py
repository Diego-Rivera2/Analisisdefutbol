from collections import UserList
from email import message
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import usuarios 
from django.contrib.auth import authenticate
from django.template import RequestContext

# Create your views here.


def index(request):
    return render(request, "registroUsuarios.html")

def login(request):
    usuario=request.POST.get('usr')
    password=request.POST.get('pwd')
    user = authenticate(username=usuario, password=password)
    

    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
       messages.warning(request, 'Credenciales Invalidas.')
       return render(request, "registroUsuarios.html")
        


def RegistroUsuarios(request):
    nombre= request.POST["nombre"]
    apellido= request.POST["apellido"]
    direccion=request.POST["direccion"]
    fecha_nac=request.POST["fecha_nac"]
    pais=request.POST["pais"]
    telef=request.POST["telef"]
    correo=request.POST["correo"]
    usuario=request.POST["usuario"]
    password=request.POST["password"]
    perfil="User"
    imagen=""
   

    usuario = usuarios.objects.create(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, direccion=direccion,pais=pais,telef=telef,correo=correo,usuario=usuario,password=password,perfil=perfil,imagen=imagen)
    return redirect("/")   


def perfil(request):   
    userList= usuarios.objects.all()
    return render(request,"perfil.html",{'usuarios':userList})


def logout_request(request):
	messages.info(request, "You have successfully logged out.") 
	return render(request, "logout.html")

def editPerfil(request,id):
    userList= usuarios.objects.get(id=id)
    return render(request,"editPerfil.html",{'usuarios':userList})

def updatePerfil(request):

    id=request.POST["id"]
    nombre= request.POST["nombre"]
    apellido= request.POST["apellido"]
    direccion=request.POST["direccion"]
    fecha_nac=request.POST["fecha_nac"]
    pais=request.POST["pais"]
    telef=request.POST["telef"]
    correo=request.POST["correo"]
    usuario=request.POST["usuario"]
    password=request.POST["password"]
    perfil=request.POST["perfil"]


    userList= usuarios.objects.get(id=id)
    userList.nombre=nombre
    userList.apellido=apellido
    userList.direccion=direccion
    userList.fecha_nac=fecha_nac
    userList.pais=pais
    userList.telef=telef
    userList.correo=correo
    userList.usuario=usuario
    userList.password=password
    userList.perfil=perfil
    userList.save()
    
    return redirect(request,"/perfil.html/")


def elimPerfil(request):
    messages.info(request,"You have successfully logged out.") 
    return render(request,"elimPerfil.html")


def about(request):
    messages.info(request, "Welcome About Us") 
    return render(request,"about.html")