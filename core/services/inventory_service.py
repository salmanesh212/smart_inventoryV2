"""Inventory service for managing products in the Smart Inventory System."""

import logging
from typing import Optional

from core.models import Product
from core.exceptions import OutOfStockException, InvalidQuantityException

logger = logging.getLogger(__name__)


class InventoryService:
    """Service layer for product inventory operations."""

    def __init__(self):
        self.products: dict[int, Product] = {}

    def add_product(self, product: Product) :
        """Add a product to the inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with id {product.id} already exists")
        self.products[product.id] = product
        logger.info("Product '%s' added to inventory", product.name)

    def get_product(self, product_id: int) :
        """Retrieve a product by its ID."""
        if product_id not in self.products:
            raise ValueError(f"Product with id {product_id} not found")
        return self.products[product_id]

    def remove_product(self, product_id: int) :
        """Remove and return a product from the inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with id {product_id} not found")
        removed = self.products.pop(product_id)
        logger.info("Product '%s' removed from inventory", removed.name)
        return removed

    def restock(self, product_id: int, qty: int) :
        """Add stock to an existing product."""
        product = self.get_product(product_id)
        product.add_stock(qty)

    def sell_stock(self, product_id: int, qty: int) :
        """Sell stock from an existing product."""
        product = self.get_product(product_id)
        product.remove_stock(qty)

    def get_all_products(self) :
        """Return all products in the inventory."""
        return list(self.products.values())

    def get_low_stock(self, threshold: int = 5) :
        """Return products with stock at or below the threshold."""
        return [p for p in self.products.values() if p.quantity_in_stock <= threshold]

    def get_total_inventory_value(self) :
        """Return the total monetary value of all inventory."""
        return sum(p.get_value_in_stock() for p in self.products.values())

    def search_by_category(self, category: str):
        """Return products matching the given category."""
        return [p for p in self.products.values() if p.category.lower() == category.lower()]

    def search_by_name(self, keyword: str) :
        """Return products whose name contains the keyword."""
        return [p for p in self.products.values() if keyword.lower() in p.name.lower()]
