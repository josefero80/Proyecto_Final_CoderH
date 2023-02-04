from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Comentario
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from blog.forms import PostUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html', )

class About(TemplateView):
    template_name = 'blog/about.html'

class PostList(ListView):
    model = Post
    template_name = 'blog/listaposts.html'


class Lista_edicion(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = Post
    success_url = reverse_lazy('lista_edicion')
    template_name = 'blog/listaEdicion.html'


class PostDetail(DetailView):
    model = Post
    success_url = reverse_lazy('homepage')
    template_name = 'blog/detalle_post.html'

class EditPost(LoginRequiredMixin, UpdateView):
    login_url = 'login_user'
    model = Post
    template_name = 'blog/editarPost.html'     
    form_class = PostUpdateForm
    success_url = reverse_lazy('lista_edicion')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else: 
            if post.autor != self.request.user:
                messages.error(request, 'No eres usuario autorizado para EDITAR el Post... ')
                return redirect('lista_edicion')
            
            return super().dispatch(request, *args, **kwargs)

class CreaPost(LoginRequiredMixin, CreateView):
    login_url = 'login_user'
    model = Post
    template_name = 'blog/creaPost.html'
    form_class = PostUpdateForm
    success_url = reverse_lazy('lista_edicion')

class EliminaPost(LoginRequiredMixin, DeleteView):
    login_url = 'login_user'
    model = Post
    template_name = 'blog/eliminaPost.html'
    success_url = reverse_lazy('lista_edicion')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else: 
            if post.autor != self.request.user:
                messages.error(request, 'No eres usuario autorizado para ELIMINAR el Post... ')
                return redirect('lista_edicion')
            
            return super().dispatch(request, *args, **kwargs)
        

