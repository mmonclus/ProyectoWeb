# Generated by Django 4.1.1 on 2022-11-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias', to='Blog.categoria'),
        ),
    ]
