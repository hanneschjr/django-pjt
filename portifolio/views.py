from django.shortcuts import render
# from .dados import habilidades, projetos
from .models import Habilidade, Projeto

# Create your views here.
def home(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'home.html', {'habilidades': habilidades})
    

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    infos = projeto.tecnologia.all()
    return render(request, 'detalhes_projeto.html', {'projeto': projeto, 'infos': infos})