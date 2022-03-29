import imp
from django import http
from django.shortcuts import render
from rest_framework import viewsets
from perfil.models import PerfilModel
from perfil.serializers import PerfilCreateSerializer, PerfilSerializer
from rest_framework.response import Response
from rest_framework import status
from perfil.service import perfilService
import service

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    service_class = perfilService()
    queryset = PerfilModel.objects.all()
    http_method_names = ["get", "post", "patch"]
 
    def create(self, request, *args, **kwargs):
        serializer = PerfilCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.service_class.busca_cep(request.data.get('cep'))
        if data is None:
            return Response({"message":"Erro ao buscar o cep"})
        data = self.service_class.create_to_save(data, request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
      