from django.db import models

# Create your models here.
class Habilidade(models.Model):
    CATEGORIAS = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('database', 'Banco de Dados'),
        ('tool', 'Ferramenta'),
        ('container', 'Containerização'),
        ('os', 'Sistema Operacional'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=30, blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outro')

    def __str__(self):
        return  self.nome
                
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    tecnologia = models.ManyToManyField(Habilidade, related_name='projetos')
    github = models.URLField(blank=True, null=True)

    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
