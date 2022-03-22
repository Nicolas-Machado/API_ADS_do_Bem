from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _ 


class Perfil(TimeStampedModel):

    class UFS(models.TextChoices):
        SC = 'SC', _('Santa Catarina')
        RS = 'RS', _('Rio Grande do Sul')
        SP = 'SP', _('São Paulo')


    nome_instituicao = models.CharField(
        max_length=50,
        db_column="NOME_INSTITUICAO",
    )

    cnpj = models.CharField(
        max_length=14,
        db_column="CNPJ",
        validators=[MaxLengthValidator(14), MinLengthValidator(14)]
    )

    logradouro = models.CharField(
        max_length=20,
        db_column="LOGRADOURO",
    )

    numero = models.CharField(
        max_length=4,
        db_column="NUMERO",
        validators=[MinLengthValidator(1), MaxLengthValidator(4)]
    )

    complemento = models.CharField(
        max_length=20,
        db_column="COMPLEMENTO",
        null=True
    )

    bairro = models.CharField(
        max_length=20,
        db_column="BAIRRO"
    )

    municipio = models.CharField(
        max_length=20,
        db_column="MUNICIPIO"
    )

    uf = models.CharField(
        max_length=2,
        db_column="UF",
        choices=UFS.choices
    )

    cep = models.CharField(
        max_length=8,
        db_column="CEP",
        validators=[MaxLengthValidator(8), MinLengthValidator(8)]
    )

    telefone = models.CharField(
        max_length=11,
        db_column="TELEFONE",
        validators=[MaxLengthValidator(11), MinLengthValidator(10)]
    )

    ano_fundacao = models.CharField(
        max_length=4,
        db_column="ANO_FUNDACAO",
        validators=[MaxLengthValidator(4), MinLengthValidator(4)]
    )

    total_membros = models.PositiveIntegerField(
        db_column="TOTAL_MEMBROS"
    )

    nome_presidente_instituicao = models.CharField(
        max_length=50,
        db_column="NOME_PRESIDENTE_INSTITUICAO"
    )

    class Meta:
        db_table = "PERFIL"
        verbose_name = "perfil"
        verbose_name_plural = "perfis"

    def __str__(self) -> str:
        return self.nome_instituicao
