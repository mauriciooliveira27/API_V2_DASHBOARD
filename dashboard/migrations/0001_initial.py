# Generated by Django 5.0.1 on 2024-01-08 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('tensao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tensao_f1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tensao_f2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tensao_f3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('corrente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('corrente_f1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('corrente_f2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_ativa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_ativa_f1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_ativa_f2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_ativa_f3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_reativa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_reativa_f1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_reativa_f2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_reativa_f3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_aparente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_aparente_f1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_aparente_f2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potencia_aparente_f3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fp_circuito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fP_fase1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fP_fase2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fP_fase3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequencia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(default=datetime.datetime.utcnow, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
