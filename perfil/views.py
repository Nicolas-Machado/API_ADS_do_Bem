import imp
from django import http
from django.shortcuts import render
from rest_framework import viewsets
from perfil.models import Perfil
from perfil.serializers import PerfilSerializer
import service

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    http_method_names = ["get", "post", "patch"]

    def create(self, request, *args, **kwargs):
        endereco = service.busca_cep()
        return super().create(request, *args, **kwargs)        