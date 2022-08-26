# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AuditoriaCuenta(models.Model):
    movimiento_id = models.AutoField(primary_key=True)
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.IntegerField()
    new_type = models.IntegerField()
    user_action = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField()
    branch = models.ForeignKey('Sucursal', on_delete = models.CASCADE, related_name='branchCliente')
    tipo = models.ForeignKey('TipoCliente', on_delete = models.CASCADE, related_name='tipoCliente')
    direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE, related_name='direccionCliente')

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.customer_name


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Cliente', on_delete = models.CASCADE, related_name='clienteCuenta')
    balance = models.FloatField()
    iban = models.TextField()
    tipo = models.ForeignKey('TipoCuenta', on_delete = models.CASCADE, related_name='tipoCuenta')

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'

    def __str__(self):
        return self.pais + ", " + self.provincia + ", " + self.ciudad + ", " + self.calle


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch = models.ForeignKey('Sucursal', on_delete = models.CASCADE, related_name='branchEmpleado')
    direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE, related_name='direccionEmpleado')

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjetas(models.Model):
    marca_id = models.AutoField(primary_key=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjetas'

    def __str__(self):
        return self.marca


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    monto = models.IntegerField()
    tipo = models.ForeignKey('TipoOperaciones', on_delete = models.CASCADE, related_name='tipoOperacion')
    hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.FloatField()
    customer = models.ForeignKey('Cliente', on_delete = models.SET_NULL, null=True, related_name='clientePrestamo')

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE, related_name='direccionSucursal')

    class Meta:
        managed = False
        db_table = 'sucursal'

    def __str__(self):
        return self.branch_name


class Tarjeta(models.Model):
    numero = models.TextField()
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.ForeignKey('TipoTarjeta', on_delete = models.CASCADE, related_name='tipoTarjeta')
    marca = models.ForeignKey('MarcaTarjetas', on_delete = models.CASCADE, related_name='marcaTarjeta')
    customer = models.ForeignKey('Cliente', on_delete = models.CASCADE, related_name='clienteTarjeta')

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

    def __str__(self):
        return self.tipo


class TipoCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

    def __str__(self):
        return self.tipo


class TipoOperaciones(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_operaciones'


class TipoTarjeta(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'

    def __str__(self):
        return self.tipo_name
