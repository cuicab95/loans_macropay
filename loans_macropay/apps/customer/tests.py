from loans_macropay.config.tests import ConfigAPITest
from .scripts import populate_dummy_data
from .models import BranchOffice, Customer, Account


class CustomerTestCase(ConfigAPITest):
    def setUp(self):
        self.user = self.create_user()
        self.authenticate(self.user)
        self.path = "/customer/process-payments/"
        populate_dummy_data()

    def test_create_dummy_data(self):
        offices = BranchOffice.objects.all()
        customers = Customer.objects.all()
        accounts = Account.objects.all()
        self.assertNotEqual(offices.count(), 0)
        self.assertNotEqual(customers.count(), 0)
        self.assertNotEqual(accounts.count(), 0)
