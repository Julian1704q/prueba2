from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre',)

admin.site.register(Producto,ProductoAdmin)

admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Categoria,CategoriaAdmin)