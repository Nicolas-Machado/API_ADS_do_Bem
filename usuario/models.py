import email
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser

from perfil.models import PerfilModel
class UsuarioModel(AbstractUser):

    email = models.EmailField(
        db_column="EMAIL",
        validators=[EmailValidator(message="Email incorreto!")],
    )

    senha = models.CharField(
        max_length=20,
        db_column="SENHA",
    )

    perfil= models.OneToOneField(
        PerfilModel, on_delete=models.CASCADE, 
        db_column="PERFIL",
        null=True
    )


class Meta:
    db_table = "USUARIO"
    verbose_name = "usuario"
    verbose_name_plural = "usuarios"