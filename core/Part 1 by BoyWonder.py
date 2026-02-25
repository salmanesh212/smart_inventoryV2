# Part 1 by BoyWonder
# Test file — imports from core/models/ and core/exceptions/ packages

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.models import Product, Customer, Order, OrderItem
from core.exceptions import OutOfStockException, InvalidEmailException, InvalidQuantityException


# Test all classes
if __name__ == "__main__":
    # Test Products
    p1 = Product(1, "Laptop", "Electronics", 1500.0, 10)
    p2 = Product(2, "Smartphone", "Electronics", 800.0, 20)
    p1.add_stock(5)
    p2.remove_stock(3)
    print(f"Product 1 value in stock: {p1.get_value_in_stock()}")

    # Test OrderItem
    oi1 = OrderItem(p1, 2)
    print(f"Subtotal for order item: {oi1.get_subtotal()}")

    # Test Customer
    c1 = Customer(1, "Alice", "alice@gmail.com")
    c2 = Customer(2, "Bob", "bob@yahoo.com")
    c1.validate_email()
    c2.validate_email()

    # Test Order
    order = Order(1, c2, "2023-10-01")
    order.add_item(p1, 2)
    order.add_item(p2, 1)
    total = order.calculate_total()
    print(f"Total order amount: {total}")
    print(f"Product 1 stock value: {p1.get_value_in_stock()}")

    # Test exceptions
    try:
        p1.remove_stock(100)
    except OutOfStockException as e:
        print(f"Caught exception: {e}")

    try:
        p1.add_stock(-5)
    except InvalidQuantityException as e:
        print(f"Caught exception: {e}")

    try:
        bad_customer = Customer(3, "Charlie", "no-email")
        bad_customer.validate_email()
    except InvalidEmailException as e:
        print(f"Caught exception: {e}")
