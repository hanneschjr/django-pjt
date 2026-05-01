from django.db import models

# Create your models here.
class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return  self.nome
                
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    tecnologia = models.ManyToManyField(Habilidade, related_name='projetos')
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

# class icone(models.Model):
#     nome = models.CharField(max_length=50)
#     desenho = models.TextField(blanck=True, null=True)

#     def __str__(self):
#         return self.nome