from django.contrib import admin
from .models import Product

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'categoria', 'data_produto','publicada')
    list_display_links = ('id',  'nome_produto', )
    search_fields = ('nome_produto', )
    list_filter = ('categoria', 'publicada', )
    list_editable = ('publicada', )
    list_per_page = 5

admin.site.register(Product, ListandoProdutos)
