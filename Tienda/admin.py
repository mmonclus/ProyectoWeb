from django.contrib import admin
from .models import Categoria_Articulo,Articulo

# Register your models here.

class Categoria_ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

admin.site.register(Categoria_Articulo,Categoria_ArticuloAdmin)   
admin.site.register(Articulo,ArticuloAdmin) 
