from pyexpat import model
from .models import UsuarioModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel

class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ('usuario', 'senha')