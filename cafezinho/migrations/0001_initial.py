# Generated by Django 5.0.3 on 2025-01-17 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contribuinte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Contribuicao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao_da_contribuicao", models.CharField(max_length=100)),
                ("data", models.DateField()),
                (
                    "contribuinte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cafezinho.contribuinte",
                    ),
                ),
            ],
        ),
    ]