from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator

# Create your views here.


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    return render(request, 'cadastrar_vendedor.html')