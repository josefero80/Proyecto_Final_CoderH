from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    campo_blog = RichTextField()
    fecha_blog = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.titulo} Autor:{self.autor}'

class Comentario(models.Model):
    nombre = models.CharField(max_length=256)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = RichTextField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.fecha}'

class Galeria(models.Model):
    id_foto = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

