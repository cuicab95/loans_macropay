from django.contrib import admin
from .models import Customer, Account, Loans, BranchOffice

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "amount",
        "status",
    )


@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "date_loan",
        "amount",
        "status",
        "branch_office",
        "branch_office",
    )


@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "iva",
    )