# Generated by Django 4.0.6 on 2022-08-12 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0013_alter_cuenta_options_alter_prestamo_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prestamo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tarjeta',
            options={'managed': False},
        ),
    ]