# Generated by Django 4.2.7 on 2025-03-28 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_reactivo_descripicion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='nombre_del_trabajador',
        ),
        migrations.AddField(
            model_name='trabajador',
            name='nombre_apellido',
            field=models.CharField(default='', max_length=255, validators=[django.core.validators.RegexValidator(message='El nombre y los apellidos deben comenzar con mayúscula, este campo solo puede contener letras', regex='^[A-Z][a-zñÑáéíóúÁÉÍÓÚ]*(?:\\s[A-Z][a-zñÑáéíóúÁÉÍÓÚ]*)*$')], verbose_name='Nombre del trabajador:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='ci',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='El carné de identidad debe contener exactamente 11 números y no contiene ningún carácter especial', regex='^\\d{11}$')], verbose_name='Carné de identidad:'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='rol_del_trabajador',
            field=models.CharField(max_length=255, verbose_name='Ocupación o cargo: '),
        ),
    ]
