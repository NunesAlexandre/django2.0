from django.shortcuts import render
#from .form import TransacaoForm


def index(request):
    return render(request, 'contas/index.html')

def cadastro(request):
    return render(request, 'contas/sistema/cadastro-clientes.html')

def contato(request):
	return render(request, 'contas/sistema/contato.html')

def sobre(request):
	return render(request, 'contas/sistema/quem-somos.html')

def novasenha(request):
	return render(request, 'contas/sistema/nova-senha.html')



