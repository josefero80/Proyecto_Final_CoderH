from django import forms
from blog.models import Post


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'autor', 'campo_blog', 'fecha_blog', 'descripcion_corta', 'imagen']
