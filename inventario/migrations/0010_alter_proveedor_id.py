# Generated by Django 4.2.3 on 2023-07-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_alter_area_hospital_options_alter_contrato_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
