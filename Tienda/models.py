from django.db import models

# Create your models here.

# Esta clase me da la categoria de los Articulos 
class Categoria_Articulo(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #esto lo agrega automaticamente 
    update=models.DateTimeField(auto_now_add=True)
    #esta clase me sirve para ponerle el nombre que yo quiera en la base de datos
    class Meta:
        verbose_name='Categoria_Articulo'
        verbose_name_plural='Categoria_Articulos'
    #para que me de el nombre de la categoria
    def __str__(self):
        return self.nombre

# Esta clase me da  los post         
class Articulo(models.Model):
     nombre=models.CharField(max_length=100)
     #relaciono las categorias con los productos
     categorias=models.ManyToManyField(Categoria_Articulo, related_name='categorias')
     imagen=models.ImageField(upload_to='tienda', null=True,blank=True)
     imagen_email=models.CharField(max_length=100, null=True,blank=True)
     precio=models.FloatField()
     disponibilidad=models.BooleanField(default=True)
     created=models.DateTimeField(auto_now_add=True) #esto lo agrega automaticamente 
     update=models.DateTimeField(auto_now_add=True)
     class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

     def __str__(self):
        return self.nombre
