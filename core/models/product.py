"""Product model for the Smart Inventory System."""

import logging
from core.exceptions import OutOfStockException, InvalidQuantityException

logger = logging.getLogger(__name__)


class Product:
    """Represents a product in the inventory."""

    def __init__(self, id: int, name: str, category: str, price: float, quantity_in_stock: int) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def add_stock(self, qty: int) -> None:
        """Add stock quantity to the product."""
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        self.quantity_in_stock += qty
        logger.info("Stock added: %d units to '%s'", qty, self.name)

    def remove_stock(self, qty: int) -> None:
        """Remove stock quantity from the product."""
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        if qty > self.quantity_in_stock:
            raise OutOfStockException(
                f"Not enough stock. Available: {self.quantity_in_stock}, requested: {qty}"
            )
        self.quantity_in_stock -= qty
        logger.info("Stock removed: %d units from '%s'", qty, self.name)

    def get_value_in_stock(self) -> float:
        """Return the total monetary value of stock (price * quantity)."""
        return self.price * self.quantity_in_stock

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}')"
