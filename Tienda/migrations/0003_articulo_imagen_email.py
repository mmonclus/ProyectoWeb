# Generated by Django 4.1.1 on 2022-12-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_rename_producto_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]