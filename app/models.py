from django.db import models

class Produto(models.Model):
    # 'blank=True, null=True' evita erros se o produto não tiver imagem cadastrada
    imagem = models.CharField(max_length=500, blank=True, null=True) 
    
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    estoque = models.IntegerField()
    desconto = models.BooleanField(default=False)
    
    # 'default=False' garante que produtos existentes não iniciem marcados como apagados
    apagado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome