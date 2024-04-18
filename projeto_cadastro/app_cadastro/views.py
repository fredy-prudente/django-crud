from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
import re

def home(request):
    return render(request, 'usuarios/home.html')

def adicionar_usuario(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/home.html')

def listagem_usuarios(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/usuarios.html', context)

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = request.POST.get('idade')
        usuario.save()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

def excluir_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/excluir_usuario.html', {'usuario': usuario})

@api_view(['GET'])
def check_nome(request):
    nome = request.query_params.get('nome')
    
    # Verifica se o nome contém apenas letras
    if not re.match("^[a-zA-ZÀ-ÖØ-öø-ÿ]+$", nome):
        return Response({'disponivel': False, 'mensagem': 'O nome deve conter apenas letras.'})
    
    # Verifica se existe algum usuário com o mesmo nome, ignorando a diferenciação entre maiúsculas e minúsculas
    if Usuario.objects.filter(nome__iexact=nome).exists():
        return Response({'disponivel': False, 'mensagem': 'Este nome já está em uso.'})
    
    return Response({'disponivel': True})




class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
