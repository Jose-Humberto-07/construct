from django.shortcuts import render
from .models import Categoria

# Create your views here.


def add_produto(request):
    categorias = Categoria.objects.all()
    return render(request, 'add_produto.html', {'categorias':categorias})
