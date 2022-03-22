from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from perfil.views import PerfilViewSet

router = routers.SimpleRouter()
router.register('perfil', PerfilViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
