from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import auth, messages
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def produto(request, produto_id):
    """
    Função produto, seleciona o produto por id, para mostrar no HTML
    OBS: Precisa de ajustes para mostrar o produto por determinada categoria
    """
    produto = get_object_or_404(Product, pk=produto_id)

    produto_a_exibir = {
        'produto': produto
    }
    return render(request, 'produtos/produto.html', produto_a_exibir)

def busca(request):
    """
    Função de busca, que realiza busca de determinado produto, que o usuário digitou
    """
    buscas = Product.objects.order_by('-nome_produto').filter(publicada=True)

    paginator = Paginator(buscas, 6)
    page = request.GET.get('page')
    busca_por_pagina = paginator.get_page(page)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        buscas = buscas.filter(nome_produto__icontains=nome_a_buscar)

    dados = {
        'buscas' : busca_por_pagina
    }

    return render(request, 'produtos/buscar.html', dados)

def sobre(request):
    """
    Função que sobre.
    Quando o usuário clicar no botão Sobre nós, rediciona para a página sobre.html
    """
    return render(request, 'empresa/sobre.html')

def carrinho(request):
    if request.user.is_authenticated:
        return render(request, 'empresa/carrinho.html')
    return redirect('index')
