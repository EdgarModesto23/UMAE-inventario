# Generated by Django 4.2.3 on 2023-07-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_area_hospital_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_hospital',
            name='edificio',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
