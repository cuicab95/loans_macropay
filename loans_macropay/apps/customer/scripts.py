from .models import Customer, BranchOffice, Account, Loans
from django.db import transaction


def populate_dummy_data():
    branch_office_data = [
        {
            "name": "Tijuana",
            "iva": 8.00,
        },
        {
            "name": "Nuevo Leon",
            "iva": 16.00,
        },
        {
            "name": "Tamaulipas",
            "iva": 10.00,
        }
    ]
    for branch_office in branch_office_data:
        BranchOffice.objects.create(**branch_office)
    customer_data = [
        {
            "first_name": "Juan",
            "last_name": "Perez",
            "rfc": "RFC1234567890",
            "curp": "CURP12345678987654",
            "contact_email": "juan@test.com",
            "phone_number": "9912345678",
            "account": {
                "amount": 15375.28,
                "status": "ACT"
            },
            "loans": [
                {
                    "date_loan": "2021-01-15",
                    "amount": 3500.00,
                    "branch_office": "tamaulipas"
                },
                {
                    "date_loan": "2021-01-24",
                    "amount": 725.00,
                    "branch_office": "tamaulipas"
                },
                {
                    "date_loan": "2021-02-05",
                    "amount": 725.00,
                    "branch_office": "tamaulipas"
                },

            ]
        },
        {
            "first_name": "Jose",
            "last_name": "Perez",
            "rfc": "RFC7659843125",
            "curp": "CURP87612908777654",
            "contact_email": "jose@test.com",
            "phone_number": "8167543241",
            "account": {
                "amount": 1000.51,
                "status": "BLO"
            },
            "loans": [
                {
                    "date_loan": "2021-01-12",
                    "amount": 380.00,
                    "status": "PAID",
                    "branch_office": "Nuevo leon"
                },
                {
                    "date_loan": "2021-01-24",
                    "amount": 725.00,
                    "status": "PAID",
                    "branch_office": "Nuevo leon"
                },
                {
                    "date_loan": "2021-02-05",
                    "amount": 725.00,
                    "branch_office": "Nuevo leon"
                },

            ]
        },
        {
            "first_name": "Emanuel",
            "last_name": "Perez",
            "rfc": "RFC1097389997",
            "curp": "CURP14893787652435",
            "contact_email": "emanuel@test.com",
            "phone_number": "9875237624",
            "account": {
                "amount": 5000.28,
                "status": "ACT"
            },
            "loans": [
                {
                    "date_loan": "2021-01-12",
                    "amount": 1500.00,
                    "branch_office": "Nuevo leon"
                },
                {
                    "date_loan": "2021-01-24",
                    "amount": 830.00,
                    "branch_office": "Nuevo leon"
                },
                {
                    "date_loan": "2021-02-05",
                    "amount": 15220.00,
                    "status": "PAID",
                    "branch_office": "Nuevo leon"
                },

            ]
        }
    ]
    for customer in customer_data:
        # Get data
        account_data = customer.pop('account', None)
        loans_data = customer.pop('loans', None)
        # Create customer
        instance = Customer.objects.create(**customer)
        # Updt account data and create
        account_data.update({'customer': instance})
        Account.objects.create(**account_data)
        # Updt loand data and create
        for loans in loans_data:
            branch_office = BranchOffice.objects.filter(name__icontains=loans.get('branch_office')).first()
            loans.update({'customer': instance, 'branch_office': branch_office})
            Loans.objects.create(**loans)


@transaction.atomic()
def run():
    populate_dummy_data()