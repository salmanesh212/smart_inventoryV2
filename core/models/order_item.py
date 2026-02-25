"""OrderItem model for the Smart Inventory System."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models.product import Product


class OrderItem:
    """Represents a single line item in an order."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        """Return the subtotal for this item (price * quantity)."""
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        return f"OrderItem(product='{self.product.name}', qty={self.quantity})"
