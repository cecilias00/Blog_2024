# Generated by Django 5.1.1 on 2024-09-26 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelTable(
            name='categorias',
            table='Categorias',
        ),
        migrations.AlterModelTable(
            name='posts',
            table='Posts',
        ),
    ]
