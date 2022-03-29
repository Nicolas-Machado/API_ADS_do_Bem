from django.contrib import admin

from usuario.models import UsuarioModel

class ListandoUsuario(admin.ModelAdmin):
    list_display = ('email')
    list_display_links = ('email')
    search_fields = ('email')
    list_filter = ('email',)
    list_per_page = 10

admin.site.register(UsuarioModel, ListandoUsuario)