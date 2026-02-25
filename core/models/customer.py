"""Customer model for the Smart Inventory System."""

import logging
from core.exceptions import InvalidEmailException

logger = logging.getLogger(__name__)


class Customer:
    """Represents a customer in the system."""

    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email

    def validate_email(self) -> None:
        """Validate the customer's email format."""
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            logger.warning("Invalid email attempt: %s", self.email)
            raise InvalidEmailException(f"Invalid email: {self.email}")
        logger.info("Email validated for customer '%s'", self.name)

    def __repr__(self) -> str:
        return f"Customer(id={self.id}, name='{self.name}')"
