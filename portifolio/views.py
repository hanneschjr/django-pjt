# from .dados import habilidades, projetos
import smtplib
import socket
from django.shortcuts import render, redirect
from .models import Habilidade, Projeto
from django.core.mail import EmailMessage
from .forms import ContatoForm
from django.conf import settings
from django.contrib import messages

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

            mensagem_completa = f"""
            Nome: {nome}
            Email: {email}

            Mensagem:
            {mensagem}
            """

            email_obj = EmailMessage(
                subject=assunto,
                body=mensagem_completa,
                from_email=settings.EMAIL_DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],
            )
            
            try:
                email_obj.send()
                messages.success(request, "Mensagem enviada com sucesso!")

            except smtplib.SMTPAuthenticationError:
                messages.error(request, "Erro de autenticação no servidor.")

            except smtplib.SMTPConnectError:
                messages.error(request, "Não foi possível conectar ao servidor.")

            except socket.timeout:
                messages.error(request, "Tempo de resposta esgotado.")

            except OSError:
                messages.error(request, "Erro de conexão de rede.")

            except Exception:
                messages.error(request, "Erro inesperado.")
                
    return redirect("home")