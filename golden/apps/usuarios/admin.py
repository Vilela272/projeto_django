from django.contrib import admin
from .models import Cliente

# Register your models here.
class ListandoClientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'nascimento')
    list_per_page = 5

admin.site.register(Cliente, ListandoClientes)
