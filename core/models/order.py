from core.exceptions import InvalidQuantityException
from core.models.order_item import OrderItem


class Order:
    def __init__(self, id, customer, order_date, items=None):
        self.id = id
        self.customer = customer
        self.order_date = order_date
        self.items = items if items is not None else []

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        item = OrderItem(product, quantity)
        self.items.append(item)
        print("Item added successfully")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_subtotal()
        return total
