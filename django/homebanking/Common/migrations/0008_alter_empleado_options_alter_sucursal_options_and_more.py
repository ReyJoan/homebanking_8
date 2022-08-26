# Generated by Django 4.0.6 on 2022-08-25 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0007_remove_cliente_branch_id_cliente_branch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branchCliente', to='Common.sucursal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direccionCliente', to='Common.direccion'),
        ),
    ]