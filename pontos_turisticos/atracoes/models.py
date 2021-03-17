from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=300)
    horario_func = models.TextField()
    idade_minina = models.IntegerField()

    def __str__(self):
        return self.nome
