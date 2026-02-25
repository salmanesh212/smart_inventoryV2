"""Data Access Objects (DAO) for the Smart Inventory System database layer."""

import logging
from typing import Any, Optional

import pymysql

logger = logging.getLogger(__name__)


class ProductDAO:
    """DAO for CRUD operations on the products table."""

    def __init__(self, conn: pymysql.connections.Connection):
        self.conn = conn

    def save(self, product: Any):
        """Insert a new product record into the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO products (product_id, name, category, price, quantity_in_stock) VALUES (%s, %s, %s, %s, %s)",
                (product.id, product.name, product.category, product.price, product.quantity_in_stock)
            )
            self.conn.commit()
            logger.info("Product '%s' saved to database", product.name)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error saving product: %s", e)
            raise

    def update(self, product: Any):
        """Update an existing product record in the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "UPDATE products SET name=%s, category=%s, price=%s, quantity_in_stock=%s WHERE product_id=%s",
                (product.name, product.category, product.price, product.quantity_in_stock, product.id)
            )
            self.conn.commit()
            logger.info("Product '%s' updated in database", product.name)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error updating product: %s", e)
            raise

    def delete(self, product_id: int):
        """Delete a product record from the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE product_id=%s", (product_id,))
            self.conn.commit()
            logger.info("Product #%d deleted from database", product_id)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error deleting product: %s", e)
            raise

    def find_by_id(self, product_id: int):
        """Find and return a product row by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
        return cursor.fetchone()


class CustomerDAO:
    """DAO for CRUD operations on the customers table."""

    def __init__(self, conn: pymysql.connections.Connection):
        self.conn = conn

    def save(self, customer: Any):
        """Insert a new customer record into the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO customers (customer_id, name, email) VALUES (%s, %s, %s)",
                (customer.id, customer.name, customer.email)
            )
            self.conn.commit()
            logger.info("Customer '%s' saved to database", customer.name)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error saving customer: %s", e)
            raise

    def update(self, customer: Any):
        """Update an existing customer record in the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "UPDATE customers SET name=%s, email=%s WHERE customer_id=%s",
                (customer.name, customer.email, customer.id)
            )
            self.conn.commit()
            logger.info("Customer '%s' updated in database", customer.name)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error updating customer: %s", e)
            raise

    def delete(self, customer_id: int):
        """Delete a customer record from the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM customers WHERE customer_id=%s", (customer_id,))
            self.conn.commit()
            logger.info("Customer #%d deleted from database", customer_id)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error deleting customer: %s", e)
            raise

    def find_by_id(self, customer_id: int):
        """Find and return a customer row by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id=%s", (customer_id,))
        return cursor.fetchone()


class OrderDAO:
    """DAO for CRUD operations on the orders and order_items tables."""

    def __init__(self, conn: pymysql.connections.Connection):
        self.conn = conn

    def save(self, order: Any):
        """Insert a new order and its items into the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)",
                (order.id, order.customer.id, order.order_date)
            )
            for item in order.items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                    (order.id, item.product.id, item.quantity)
                )
            self.conn.commit()
            logger.info("Order #%d saved to database", order.id)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error saving order: %s", e)
            raise

    def update(self, order: Any):
        """Update an existing order and replace its items."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "UPDATE orders SET customer_id=%s, order_date=%s WHERE order_id=%s",
                (order.customer.id, order.order_date, order.id)
            )
            cursor.execute("DELETE FROM order_items WHERE order_id=%s", (order.id,))
            for item in order.items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                    (order.id, item.product.id, item.quantity)
                )
            self.conn.commit()
            logger.info("Order #%d updated in database", order.id)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error updating order: %s", e)
            raise

    def delete(self, order_id: int):
        """Delete an order record from the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM orders WHERE order_id=%s", (order_id,))
            self.conn.commit()
            logger.info("Order #%d deleted from database", order_id)
        except Exception as e:
            self.conn.rollback()
            logger.error("Error deleting order: %s", e)
            raise

    def find_by_id(self, order_id: int):
        """Find and return an order row by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id=%s", (order_id,))
        return cursor.fetchone()




