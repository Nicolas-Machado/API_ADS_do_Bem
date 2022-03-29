from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _ 


class PerfilModel(TimeStampedModel):

    class UFS(models.TextChoices):
        AC = 'AC', _('Acre')
        AL = 'AL', _('Alagoas')
        AP = 'AP', _('Amapa')
        AM = 'AM', _('Amazonas')
        BA = 'BA', _('Bahia')
        CE = 'CE', _('Ceara')
        ES = 'ES', _('Espirito Santo')
        GO = 'GO', _('Goias')
        MA = 'MA', _('Maranhão')
        MT = 'MT', _('Mato Grosso')
        MS = 'MS', _('Mato Grosso do Sul')
        MG = 'MG', _('Minas Gerais')
        PA = 'PA', _('Para')
        PB = 'PB', _('Paraiba')
        PR = 'PR', _('Parana')
        PE = 'PE', _('Pernambuco')
        PI = 'PI', _('Piaui')
        RJ = 'RJ', _('Rio de Janeiro')
        RN = 'RN', _('Rio Grande do Norte')
        RS = 'RS', _('Rio Grande Do Sul')
        RO = 'RO', _('Rondônia')
        RR = 'RR', _('Roraima')
        SC = 'SC', _('Santa Catarina')
        SP = 'SP', _('São Paulo')
        SE = 'SE', _('Sergipe')
        TO = 'TO', _('Tocantins')
        DF = 'DF', _('Distrito Federal')



    nome_instituicao = models.CharField(
        max_length=50,
        db_column="NOME_INSTITUICAO",
        null=True,
    )

    cnpj = models.CharField(
        max_length=14,
        db_column="CNPJ",
        validators=[MaxLengthValidator(14), MinLengthValidator(14)],
        null=True,
    )

    logradouro = models.CharField(
        max_length=20,
        db_column="LOGRADOURO",
        null=True,
    )

    numero = models.CharField(
        max_length=4,
        db_column="NUMERO",
        validators=[MinLengthValidator(1), MaxLengthValidator(4)],
        null=True
    )

    complemento = models.CharField(
        max_length=20,
        db_column="COMPLEMENTO",
        null=True
    )

    bairro = models.CharField(
        max_length=20,
        db_column="BAIRRO",
        null=True,
    )

    municipio = models.CharField(
        max_length=20,
        db_column="MUNICIPIO",
        null=True,
    )

    uf = models.CharField(
        max_length=2,
        db_column="UF",
        choices=UFS.choices,
        null=True,
    )

    cep = models.CharField(
        max_length=8,
        db_column="CEP",
        validators=[MaxLengthValidator(8), MinLengthValidator(8)],
        null=True,
    )

    telefone = models.CharField(
        max_length=11,
        db_column="TELEFONE",
        validators=[MaxLengthValidator(11), MinLengthValidator(10)],
        null=True,
    )

    ano_fundacao = models.CharField(
        max_length=4,
        db_column="ANO_FUNDACAO",
        validators=[MaxLengthValidator(4), MinLengthValidator(4)],
        null=True,
    )

    total_membros = models.PositiveIntegerField(
        db_column="TOTAL_MEMBROS",
        null=True,
    )

    nome_presidente_instituicao = models.CharField(
        max_length=50,
        db_column="NOME_PRESIDENTE_INSTITUICAO",
        null=True,
    )

    class Meta:
        db_table = "PERFIL"
        verbose_name = "perfil"
        verbose_name_plural = "perfis"

    def __str__(self) -> str:
        return self.nome_instituicao
