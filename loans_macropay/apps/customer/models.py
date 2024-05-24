from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class StatusChoices(models.TextChoices):
    PENDING = "PEND", "Pendiente"
    PAID = "PAID", "Pagado"


class AccountStatusChoices(models.TextChoices):
    ACTIVE = "ACT", "Activa"
    BLOCKED = "BLO", "Bloqueada"
    CANCELED = "CAN", "Cancelada"

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)
    rfc = models.CharField(max_length=13)
    curp = models.CharField(max_length=18)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class BranchOffice(models.Model):
    name = models.CharField(max_length=100)
    iva = models.FloatField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"


class Loans(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="loans")
    date_loan = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.CASCADE, related_name="branches")
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"


class Account(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="accounts")
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=AccountStatusChoices.choices)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"




