import email
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import EmailValidator

from perfil.models import PerfilModel
class UsuarioModel(TimeStampedModel):

    email = models.EmailField(
        db_column="EMAIL",
        validators=[EmailValidator(message="Email incorreto!")],
    )

    senha = models.CharField(
        max_length=20,
    )

    perfil= models.OneToOneField(
        PerfilModel, on_delete=models.CASCADE, db_column="PERFIL"
    )