from .models import PerfilModel
from rest_framework import serializers

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel
        exclude = ('modified', 'created')

class PerfilCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel
        fields = ('nome_instituicao', 'cep', 'cnpj')

