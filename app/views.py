from django.shortcuts import render
from .models import Produto

# Create your views here.
def home_view(request):
    context = {

    }
    return render(request,'home.html', context)

def perfil_view(request):
    context = {
        'nome_funcionario': 'Gustavo',
        'cargo': 'Professor',
        'setor': 'T.I.',
    }
    return render(request,'perfil.html', context)

def produtos_view(request):
    produtos = Produto.objects.all()

    context = {
        'produtos':produtos
    }

    return render(request,'produtos.html', context)
