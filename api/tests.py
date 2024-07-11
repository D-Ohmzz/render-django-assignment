from django.test import TestCase
from .models import Customer, Order

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Customer Test", phone_number="+254733333333")

    def test_customer_creation(self):
        customer = Customer.objects.get(phone_number="+254733333333")
        self.assertEqual(customer.name, "Customer Test")

class OrderTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Customer Test2", phone_number="+254722222222")
        Order.objects.create(customer=customer, item="Laptop", amount=1500)

    def test_order_creation(self):
        order = Order.objects.get(item="Laptop")
        self.assertEqual(order.amount, 1500)