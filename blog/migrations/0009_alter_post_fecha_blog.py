# Generated by Django 4.1.4 on 2023-01-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_blog',
            field=models.DateField(),
        ),
    ]
