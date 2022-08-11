# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='old_type', blank=True, null=True)
    new_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='new_type', blank=True, null=True)
    user_action = models.TextField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo = models.ForeignKey('TipoCliente', models.DO_NOTHING)
    propietario_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class ConjuntoDirecciones(models.Model):
    conjunto_direcciones_id = models.AutoField(blank=True, null=True)
    propietario_id = models.IntegerField()
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conjunto_direcciones'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo = models.ForeignKey('TipoCuenta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True, blank=True, null=True)
    calle = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    propietario_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjetas(models.Model):
    marca_id = models.AutoField(primary_key=True, blank=True, null=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjetas'


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    tipo = models.ForeignKey('TipoOperaciones', models.DO_NOTHING, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.TextField()
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.ForeignKey('TipoTarjeta', models.DO_NOTHING)
    marca = models.ForeignKey(MarcaTarjetas, models.DO_NOTHING)
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class TipoOperaciones(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_operaciones'


class TipoTarjeta(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'
