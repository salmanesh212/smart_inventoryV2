"""Unit tests for the core business logic of the Smart Inventory System."""

import unittest

from core.models.product import Product
from core.models.customer import Customer
from core.models.order import Order
from core.models.order_item import OrderItem
from core.exceptions import (
    OutOfStockException,
    InvalidEmailException,
    InvalidQuantityException,
)


class TestProduct(unittest.TestCase):
    """Tests for the Product model."""

    def setUp(self):
        """Create a sample product for each test."""
        self.product = Product(id=1, name="Laptop", category="Electronics",
                               price=999.99, quantity_in_stock=10)

    def test_add_stock(self):
        """Adding valid stock increases quantity."""
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity_in_stock, 15)

    def test_add_stock_invalid(self):
        """Adding zero or negative stock raises InvalidQuantityException."""
        with self.assertRaises(InvalidQuantityException):
            self.product.add_stock(0)
        with self.assertRaises(InvalidQuantityException):
            self.product.add_stock(-3)

    def test_remove_stock(self):
        """Removing valid stock decreases quantity."""
        self.product.remove_stock(4)
        self.assertEqual(self.product.quantity_in_stock, 6)

    def test_remove_stock_exceeds(self):
        """Removing more than available raises OutOfStockException."""
        with self.assertRaises(OutOfStockException):
            self.product.remove_stock(20)

    def test_remove_stock_invalid(self):
        """Removing zero or negative stock raises InvalidQuantityException."""
        with self.assertRaises(InvalidQuantityException):
            self.product.remove_stock(0)

    def test_get_value_in_stock(self):
        """Stock value equals price * quantity."""
        self.assertAlmostEqual(self.product.get_value_in_stock(), 9999.90, places=2)

    def test_repr(self):
        """String representation is readable."""
        self.assertIn("Laptop", repr(self.product))


class TestCustomer(unittest.TestCase):
    """Tests for the Customer model."""

    def test_valid_email(self):
        """A properly formatted email does not raise."""
        customer = Customer(id=1, name="Alice", email="alice@example.com")
        customer.validate_email()  # should not raise

    def test_invalid_email_no_at(self):
        """Email without '@' raises InvalidEmailException."""
        customer = Customer(id=2, name="Bob", email="bobexample.com")
        with self.assertRaises(InvalidEmailException):
            customer.validate_email()

    def test_invalid_email_no_dot(self):
        """Email without '.' in domain raises InvalidEmailException."""
        customer = Customer(id=3, name="Carol", email="carol@examplecom")
        with self.assertRaises(InvalidEmailException):
            customer.validate_email()

    def test_repr(self):
        """String representation includes name."""
        customer = Customer(id=1, name="Alice", email="alice@example.com")
        self.assertIn("Alice", repr(customer))


class TestOrderItem(unittest.TestCase):
    """Tests for the OrderItem model."""

    def test_get_subtotal(self):
        """Subtotal equals price * quantity."""
        product = Product(id=1, name="Mouse", category="Electronics",
                          price=25.00, quantity_in_stock=50)
        item = OrderItem(product=product, quantity=3)
        self.assertAlmostEqual(item.get_subtotal(), 75.00, places=2)

    def test_repr(self):
        """String representation includes product name."""
        product = Product(id=1, name="Mouse", category="Electronics",
                          price=25.00, quantity_in_stock=50)
        item = OrderItem(product=product, quantity=3)
        self.assertIn("Mouse", repr(item))


class TestOrder(unittest.TestCase):
    """Tests for the Order model."""

    def setUp(self):
        """Create sample objects for each test."""
        self.customer = Customer(id=1, name="Alice", email="alice@example.com")
        self.product1 = Product(id=1, name="Keyboard", category="Electronics",
                                price=50.00, quantity_in_stock=30)
        self.product2 = Product(id=2, name="Monitor", category="Electronics",
                                price=300.00, quantity_in_stock=10)
        self.order = Order(id=1, customer=self.customer, order_date="2025-06-01")

    def test_add_item(self):
        """Adding an item increases order item count."""
        self.order.add_item(self.product1, 2)
        self.assertEqual(len(self.order.items), 1)

    def test_add_item_invalid_quantity(self):
        """Adding an item with invalid quantity raises exception."""
        with self.assertRaises(InvalidQuantityException):
            self.order.add_item(self.product1, 0)

    def test_calculate_total(self):
        """Total sums all item subtotals."""
        self.order.add_item(self.product1, 2)   # 100
        self.order.add_item(self.product2, 1)   # 300
        self.assertAlmostEqual(self.order.calculate_total(), 400.00, places=2)

    def test_calculate_total_empty(self):
        """Empty order has zero total."""
        self.assertEqual(self.order.calculate_total(), 0)

    def test_repr(self):
        """String representation includes customer name."""
        self.assertIn("Alice", repr(self.order))


if __name__ == '__main__':
    unittest.main()
