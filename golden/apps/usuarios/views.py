from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Cliente

# Create your views here.

def cadastro(request):
    """
    Função para realizar cadastro de um novo usuário no sistema
    """
    if request.method == 'POST':
        usuario = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        email2 = request.POST['email2']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(usuario) or usuario is None:
            messages.error(request, 'O campo usuário não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(nome) or nome == None:
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(sobrenome) or sobrenome == None:
            messages.error(request, 'O campo sobrenome não pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email) or email == None:
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email2) or email2 == None:
            messages.error(request, 'O campo confirmação de email não pode ficar em branco')
            return redirect('cadastro')

        if email_nao_sao_iguais(email, email2):
            messages.error(request, 'O campo de e-mail e confirmação de e-mail não são iguais')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'O campo de senha e confirmação de senha não conferem')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Este nome de usuário ja existe. Por favor, insira outro')
            return redirect('cadastro')
        user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """
    Função que faz a validação do login do usuário, login é permitido com e-mail e senha
    """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
       
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'ATENÇÃO!!! Campo e-mail e/ou senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('index')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'ATENÇÃO!!! E-mail e/ou senha inválidos')
        else:
            messages.error(request, 'ATENÇÃO!!! Este e-mail não está cadastrado')
    return render(request, 'usuarios/login.html')

def logout(request):
    """
    Função que faz o logout do usuário do sistema
    """
    auth.logout(request)
    messages.warning(request, 'Logout realizado com sucesso!!!')
    return redirect('login')

def enviar_email(request):
    """
    Função não utilizada no momento, 
    mas se for necessário, rediciona o usuário para a página do email
    """
    if request.user.is_authenticated:
        return render(request, 'usuarios/email.html')
    return redirect('index')

def recuperar_senha(request):
    return render(request, 'usuarios/recupersenha.html')

def carrinho(request):
    """
    Função que verifica se o usuário está logado, e pode acessar o carrinho de compras
    """
    if request.user.is_authenticated:
        return render(request, 'empresa/carrinho.html')
    return redirect('index')

def campo_vazio(campo):
    """
    Função que verifica se um determinado campo, de cadastro ou login está vazio
    """
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """
    Função que verifica se as senha são diferentes para realizar o cadastro
    """
    return senha != senha2

def email_nao_sao_iguais(email, email2):
    """
    Função que verifica se os emails não são iguais para realizar o cadastro
    """
    return email != email2
