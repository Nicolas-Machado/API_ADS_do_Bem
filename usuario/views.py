import imp
from django import http
from django.shortcuts import render
from rest_framework import viewsets
from usuario.models import UsuarioModel
from usuario.serializers import UsuarioSerializer, UsuarioCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from perfil.models import PerfilModel
from perfil.service import UsuarioService


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = UsuarioModel.objects.all()
    http_method_names = ["get", "post", "patch"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(PerfilModel)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UsuarioCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
