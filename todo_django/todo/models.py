from django.db import models

# Create your models here.

from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    finalizada = models.BooleanField(default=False)
