from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comentario
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.forms import PostUpdateForm


# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html', )

class PostList(ListView):
    model = Post
    template_name = 'blog/listaposts.html'

# def Lista_edicion(request):
#     pass
class Lista_edicion(ListView):
    model = Post
    template_name = 'blog/listaEdicion.html'


class PostDetail(DetailView):
    model = Post
    success_url = reverse_lazy('homepage')
    template_name = 'blog/detalle_post.html'

class EditPost(UpdateView):
    model = Post
    template_name = 'blog/editarPost.html'     
    form_class = PostUpdateForm
    success_url = reverse_lazy('lista_edicion')

class CreaPost(CreateView):
    model = Post
    template_name = 'blog/creaPost.html'
    form_class = PostUpdateForm
    success_url = reverse_lazy('lista_edicion')

class EliminaPost(DeleteView):
    model = Post
    template_name = 'blog/eliminaPost.html'
    success_url = reverse_lazy('lista_edicion')
