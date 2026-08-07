from django.shortcuts import redirect, render
from.models import Produto
from .forms import ProdutoForm

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

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()

    context = {
        'produtos': produtos,
        'form': form
    }
    return render(request,'produtos.html', context)

