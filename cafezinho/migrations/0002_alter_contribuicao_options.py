# Generated by Django 5.0.3 on 2025-01-17 02:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafezinho", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contribuicao",
            options={
                "ordering": ["data"],
                "verbose_name": "Contribuição",
                "verbose_name_plural": "Contribuições",
            },
        ),
    ]
