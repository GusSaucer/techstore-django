from django.shortcuts import redirect, render, get_object_or_404
from.models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileUpdateForm


# Create your views here.
def home_view(request):
    context = {
        
    }
    return render(request,'home.html', context)

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'perfil.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def produtos_view(request):
    # Opcional: filtrar direto no banco produtos não apagados -> Produto.objects.filter(apagado=False)
    produtos = Produto.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update':
            produto_id = request.POST.get('produto_id')
            produto = get_object_or_404(Produto, id=produto_id)
            
            # Copia os dados do POST para incluir o tratamento das checkboxes
            data = request.POST.copy()
            data['desconto'] = 'desconto' in request.POST
            data['apagado'] = 'apagado' in request.POST

            form = ProdutoForm(data, instance=produto)
            if form.is_valid():
                form.save()
                return redirect('produtos')

        else:
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
    return render(request, 'produtos.html', context)

