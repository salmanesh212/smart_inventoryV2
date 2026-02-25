"""Order model for the Smart Inventory System."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Optional

from core.exceptions import InvalidQuantityException
from core.models.order_item import OrderItem

if TYPE_CHECKING:
    from core.models.product import Product
    from core.models.customer import Customer

logger = logging.getLogger(__name__)


class Order:
    """Represents a customer order containing one or more items."""

    def __init__(self, id: int, customer: Customer, order_date: str,
                 items: Optional[list[OrderItem]] = None):
        self.id = id
        self.customer = customer
        self.order_date = order_date
        self.items: list[OrderItem] = items if items is not None else []

    def add_item(self, product: Product, quantity: int) -> None:
        """Add a product with a given quantity to the order."""
        if quantity <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        item = OrderItem(product, quantity)
        self.items.append(item)
        logger.info("Item '%s' x%d added to Order #%d", product.name, quantity, self.id)

    def calculate_total(self) -> float:
        """Calculate and return the total cost of the order."""
        return sum(item.get_subtotal() for item in self.items)

    def __repr__(self) -> str:
        return f"Order(id={self.id}, customer='{self.customer.name}', items={len(self.items)})"
