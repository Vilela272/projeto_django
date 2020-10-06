from django.contrib import admin
from .models import Categorias

# Register your models here.
class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'publicada')
    list_display_links = ('id',  'nome_categoria' )
    search_fields = ('id', 'nome_categoria', )
    list_filter = ('nome_categoria', )
    list_editable = ('publicada', )
    list_per_page = 3

admin.site.register(Categorias, ListandoCategorias)
