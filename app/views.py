from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'instrutor': 'Diego',
        'curso': 'Front-end',
        'carga_horaria': '20 horas',
        'nivel': 'Iniciante'
    }
    # Caminho com namespace
    return render(request,'home.html', context)
