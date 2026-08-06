from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200) #CharField = tipo string
    preco = models.FloatField() # tipo float
    estoque = models.IntegerField() # tipo inteiro
    desconto = models.BooleanField() # tipo booleano
    def __str__(self): # Método Getter (POO)
        return self.nome

