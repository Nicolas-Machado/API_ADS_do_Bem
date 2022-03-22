# Generated by Django 4.0.3 on 2022-03-22 00:21

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome_instituicao', models.CharField(db_column='NOME_INSTITUICAO', max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.MinLengthValidator(14)])),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=14, validators=[django.core.validators.MaxLengthValidator(14), django.core.validators.MinLengthValidator(14)])),
                ('logradouro', models.CharField(db_column='LOGRADOURO', max_length=20, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.MinLengthValidator(20)])),
                ('numero', models.CharField(db_column='NUMERO', max_length=4, validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(4)])),
                ('complemento', models.CharField(db_column='COMPLEMENTO', max_length=20, null=True)),
                ('bairro', models.CharField(db_column='BAIRRO', max_length=20)),
                ('municipio', models.CharField(db_column='MUNICIPIO', max_length=20)),
                ('uf', models.CharField(choices=[('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('SP', 'São Paulo')], db_column='UF', max_length=2)),
                ('cep', models.CharField(db_column='CEP', max_length=8, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.MinLengthValidator(8)])),
                ('telefone', models.CharField(db_column='TELEFONE', max_length=11, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(10)])),
                ('ano_fundacao', models.CharField(db_column='ANO_FUNDACAO', max_length=4, validators=[django.core.validators.MaxLengthValidator(4), django.core.validators.MinLengthValidator(4)])),
                ('total_membros', models.PositiveIntegerField(db_column='TOTAL_MEMBROS')),
                ('nome_presidente_instituicao', models.CharField(db_column='NOME_PRESIDENTE_INSTITUICAO', max_length=50)),
            ],
            options={
                'verbose_name': 'endereco',
                'verbose_name_plural': 'enderecos',
                'db_table': 'PERFIL',
            },
        ),
    ]
