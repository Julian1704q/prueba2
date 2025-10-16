from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.CharField()

    def __str__(self):
        return self.nombre