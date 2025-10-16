from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def inicio(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'inicio.html', context)


def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    context = {
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'categoria.html', context)


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    context = {
        'producto': producto,
        'categorias': categorias,
    }
    return render(request, 'detalle.html', context)
