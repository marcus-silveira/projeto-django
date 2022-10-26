from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    contexto = {
        'produtos': produtos
    }
    return render(request, 'core/layouts/index.html', contexto)


def contato(request):
    return render(request, 'core/layouts/contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'core/layouts/produto.html', context)
