from django.shortcuts import render
#from .form import TransacaoForm


def index(request):
    return render(request, 'contas/index.html')

def cadastro(request):
    return render(request, 'contas/cadastro-clientes.html')

def contato(request):
	return render(request, 'contas/contato.html')

def sobre(request):
	return render(request, 'contas/quem-somos.html')

def novasenha(request):
	return render(request, 'contas/nova-senha.html')

def base(request):
	return render(request, 'contas/base.html')




