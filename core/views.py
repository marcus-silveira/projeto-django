from django.shortcuts import render


def index(request):
    return render(request, 'core/layouts/index.html')


def contato(request):
    return render(request, 'core/layouts/contato.html')
