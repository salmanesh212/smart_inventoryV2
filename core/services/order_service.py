"""Order service for managing orders in the Smart Inventory System."""

import logging
from datetime import datetime
from typing import Any

from core.models import Order, OrderItem, Customer, Product
from core.exceptions import InvalidQuantityException, OutOfStockException
from core.services.inventory_service import InventoryService

logger = logging.getLogger(__name__)


class OrderService:
    """Service layer for order operations."""

    def __init__(self, inventory_service: InventoryService):
        self.orders: dict[int, Order] = {}
        self.inventory_service = inventory_service
        self._next_order_id: int = 1

    def create_order(self, customer: Customer):
        """Create a new order for the given customer."""
        customer.validate_email()
        order = Order(self._next_order_id, customer, datetime.now().strftime("%Y-%m-%d"))
        self.orders[order.id] = order
        self._next_order_id += 1
        logger.info("Order #%d created for '%s'", order.id, customer.name)
        return order

    def add_item_to_order(self, order_id: int, product_id: int, quantity: int):
        """Add a product to an existing order, reducing inventory stock."""
        order = self.get_order(order_id)
        product = self.inventory_service.get_product(product_id)
        product.remove_stock(quantity)
        order.add_item(product, quantity)
        return order

    def get_order(self, order_id: int):
        """Retrieve an order by its ID."""
        if order_id not in self.orders:
            raise ValueError(f"Order with id {order_id} not found")
        return self.orders[order_id]

    def get_all_orders(self):
        """Return all orders."""
        return list(self.orders.values())

    def get_orders_by_customer(self, customer_id: int):
        """Return all orders belonging to a specific customer."""
        return [o for o in self.orders.values() if o.customer.id == customer_id]

    def get_order_summary(self, order_id: int):
        """Return a summary dictionary for the given order."""
        order = self.get_order(order_id)
        return {
            "order_id": order.id,
            "customer": order.customer.name,
            "date": order.order_date,
            "items": [
                {
                    "product": item.product.name,
                    "quantity": item.quantity,
                    "subtotal": item.get_subtotal(),
                }
                for item in order.items
            ],
            "total": order.calculate_total(),
        }
