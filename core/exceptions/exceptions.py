"""Custom exceptions for the Smart Inventory System."""


class OutOfStockException(Exception):
    """Raised when there is not enough stock to fulfill a request."""

    def __init__(self, message: str = "Not enough stock available"):
        super().__init__(message)


class InvalidEmailException(Exception):
    """Raised when an email address is invalid."""

    def __init__(self, message: str = "Invalid email address"):
        super().__init__(message)


class InvalidQuantityException(Exception):
    """Raised when quantity is not a positive number."""

    def __init__(self, message: str = "Quantity must be positive"):
        super().__init__(message)
