from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegisterForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_edicion')

        else:
            messages.success(request, ("Usuario o contraseña Inválidos intente nuevamente"))
            return redirect('login_user')

    else:
        return render(request, 'accounts/areaMembers.html', {} )

class Logout_user(LogoutView):
    template_name = 'accounts/logout.html'

def Registrar_usuario(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Tu registro ha sido exitoso.... "))
            return redirect('lista_edicion')
             
  
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/registrarUsuario.html', {'form': form}, )
