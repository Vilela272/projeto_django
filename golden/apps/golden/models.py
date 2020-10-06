from django.db import models
from datetime import datetime
from categorias.models import Categorias
from django.contrib.auth.models import User


class Product(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=200)
    descricao = models.TextField()
    design_produto = models.TextField()
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    tamanho_um = models.CharField('Tamanhos', max_length=5, blank=True, null=False, default='P')
    tamanho_dois = models.CharField('Tamanhos', max_length=5, blank=True, null=False, default='M')
    tamanho_tres = models.CharField('Tamanhos', max_length=5, blank=True, null=False, default='G')
    tamanho_quatro = models.CharField('Tamanhos', max_length=5, blank=True, null=False, default='GG')
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_produto
