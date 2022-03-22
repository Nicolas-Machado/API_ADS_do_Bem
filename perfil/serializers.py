from .models import Perfil
from rest_framework import serializers

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        exclude = ('modified', 'created')