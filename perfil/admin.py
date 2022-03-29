from django.contrib import admin
from .models import PerfilModel

class ListandoPerfil(admin.ModelAdmin):
    list_display = ('nome_instituicao', 'cnpj', 'logradouro', 'numero',)
    list_display_links = ('nome_instituicao', 'cnpj',)
    search_fields = ('nome_instituicao', 'cnpj',)
    list_filter = ('nome_instituicao', 'cnpj',)
    list_per_page = 10

admin.site.register(PerfilModel, ListandoPerfil)