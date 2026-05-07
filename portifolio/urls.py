from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('detalhes_projeto/<str:id_projeto>/', views.detalhes_projeto, name='detalhes_projeto'),
    path("send-email/", views.send_email_view,  name="send_email"
),
]