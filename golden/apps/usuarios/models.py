from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    email2 = models.EmailField(max_length=100)
    senha = models.CharField(max_length=20)
    senha2 = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    nascimento = models.DateField(blank=True)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
