# Generated by Django 4.2.4 on 2023-10-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporteusuario',
            name='equipo_complementario',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
