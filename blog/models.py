from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    categoria = models.CharField(max_length=256, null=True)
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    campo_blog = RichTextField(null=True)
    fecha_blog = models.DateTimeField()
    descripcion_corta= models.TextField(null=True)
    imagen = models.ImageField(upload_to="ImgPost", null=True)

    def __str__(self) -> str:
        return f'{self.titulo} Autor:{self.autor}'

class Comentario(models.Model):
    nombre = models.CharField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    comentario = RichTextField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.fecha}'


