from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Categorias
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    """
    Funão index.
    Conforme o Admin criar a categoria, e ela estiver pulicada (publicada=True)
    irá aparecer na página home do sistema.
    E também foi implementado uma paginação, de só aparecer 6 categorias por página
    """
    categorias = Categorias.objects.order_by('nome_categoria').filter(publicada=True)

    paginator = Paginator(categorias, 6)
    page = request.GET.get('page')
    categorias_por_pagina = paginator.get_page(page)

    dados = {
        'categorias' : categorias_por_pagina
    }
    return render(request, 'categorias/index.html',  dados)

def categoria(request, categoria_id):
    """
    Função categoria.
    Realiza a busca da categoria por id
    """
    categoria = get_object_or_404(Categorias, pk=categoria_id)

    categoria_a_exibir = {
        'categoria': categoria
    }
    return render(request, 'categorias/index.html', categoria_a_exibir)

