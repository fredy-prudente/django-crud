from rest_framework import serializers
from .models import Usuario
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome', 'idade']
