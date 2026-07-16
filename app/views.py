from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'nome_empresa': 'TechStore 🐸',
        'produtos': ['Smartphone', 'PC Gamer', 'Monitor', 'Smartwatch', 'Cadeira Gamer']
    }
    return render(request,'home.html', context)

def perfil_view(request):
    context = {
        'nome_funcionario': 'Gustavo',
        'cargo': 'Professor',
        'setor': 'T.I.',
    }
    return render(request,'perfil.html', context)

def status_view(request):
    context = {
        'id_servidor': '145761',
        'status_sistema': '200 OK',
        'admin':False,
    }
    return render(request,'status.html', context)
