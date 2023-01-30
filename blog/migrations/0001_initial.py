# Generated by Django 4.1.4 on 2023-01-15 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField()),
            ],
        ),

        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('autor', models.CharField(max_length=256)),
                ('campo_blog', models.TextField()),
                ('fecha_blog', models.DateTimeField(null=True)),
            ],
        ),
    ]
