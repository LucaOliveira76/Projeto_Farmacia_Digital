from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.urls import reverse

class Medicamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Receita(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    medicacoes = models.ManyToManyField(Medicamento)
    cronograma = models.TextField(null=True)