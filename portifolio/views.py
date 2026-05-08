from django.shortcuts import render, redirect
# from .dados import habilidades, projetos
from .models import Habilidade, Projeto
from django.core.mail import send_mail
from .forms import ContatoForm

# Create your views here.
def home(request):
    habilidades = Habilidade.objects.all()
    form = ContatoForm()
    return render(request, 'home.html', {'habilidades': habilidades, "contact_form": form})
    

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    infos = projeto.tecnologia.all()
    return render(request, 'detalhes_projeto.html', {'projeto': projeto, 'infos': infos})

def send_email_view(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            assunto = form.cleaned_data["assunto"]
            mensagem = form.cleaned_data["mensagem"]

            send_mail(
                nome=nome,
                assunto=assunto,
                mensagem=mensagem,
                from_email=email,
                recipient_list=["seuemail@email.com"]
            )

    return redirect("home")