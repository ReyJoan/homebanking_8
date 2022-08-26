# Generated by Django 4.0.6 on 2022-08-25 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0013_alter_movimientos_options_prestamo_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={},
        ),
        migrations.RemoveField(
            model_name='movimientos',
            name='tipo_id',
        ),
        migrations.AddField(
            model_name='movimientos',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tipoOperacion', to='Common.tipooperaciones'),
            preserve_default=False,
        ),
    ]