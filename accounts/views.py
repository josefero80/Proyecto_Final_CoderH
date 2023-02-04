from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegisterForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from accounts.forms import UserUpdateForm, UserDetail
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class UserDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login_user'
    model = User
    form_class = UserDetail
    success_url = reverse_lazy('lista_edicion')
    template_name = "accounts/profile.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login_user'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('homepage')
    template_name = 'accounts/editar_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
    


