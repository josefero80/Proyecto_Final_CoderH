from django.urls import path
from blog.views import PostDetail, PostList, Lista_edicion, EditPost, CreaPost, EliminaPost, About

urlpatterns = [
    path('pages/', PostList.as_view(), name="lista_posts"),
    path('about/', About.as_view(), name="about"),
    path('lista-editar/', Lista_edicion.as_view(), name="lista_edicion"),
    path('pages/<int:pk>/', PostDetail.as_view(), name="detalle_post"),
    path('pages/editar/<int:pk>/', EditPost.as_view(), name="editar_post"),
    path('pages/crear-post/', CreaPost.as_view(), name="crear_post"),
    path('pages/elimina-post/<int:pk>/', EliminaPost.as_view(), name="elimina_post"),

]
