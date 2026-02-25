"""Customer service for managing customers in the Smart Inventory System."""

import logging

from core.models import Customer
from core.exceptions import InvalidEmailException

logger = logging.getLogger(__name__)


class CustomerService:
    """Service layer for customer operations."""

    def __init__(self) :
        self.customers: dict[int, Customer] = {}
        self._next_id: int = 1

    def register_customer(self, name: str, email: str):
        """Register a new customer after validating their email."""
        customer = Customer(self._next_id, name, email)
        customer.validate_email()
        if any(c.email == email for c in self.customers.values()):
            raise ValueError(f"Customer with email '{email}' already exists")
        self.customers[customer.id] = customer
        self._next_id += 1
        logger.info("Customer '%s' registered successfully", name)
        return customer

    def get_customer(self, customer_id: int):
        """Retrieve a customer by their ID."""
        if customer_id not in self.customers:
            raise ValueError(f"Customer with id {customer_id} not found")
        return self.customers[customer_id]

    def get_all_customers(self):
        """Return all registered customers."""
        return list(self.customers.values())

    def search_by_name(self, keyword: str):
        """Return customers whose name contains the keyword."""
        return [c for c in self.customers.values() if keyword.lower() in c.name.lower()]

    def remove_customer(self, customer_id: int) :
        """Remove and return a customer by their ID."""
        if customer_id not in self.customers:
            raise ValueError(f"Customer with id {customer_id} not found")
        removed = self.customers.pop(customer_id)
        logger.info("Customer '%s' removed", removed.name)
        return removed
