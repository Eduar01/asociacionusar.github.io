# Generated by Django 3.2.8 on 2022-10-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_auto_20221020_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='telefono',
            field=models.CharField(max_length=9, null=True, verbose_name='Telefono'),
        ),
    ]