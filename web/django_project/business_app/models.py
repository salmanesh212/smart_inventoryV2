"""Django ORM models for the Smart Inventory System."""

from decimal import Decimal

from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    """Represents a product in the inventory."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    """Represents a registered customer."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def clean(self) -> None:
        """Validate the customer's email format."""
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ValidationError({"email": "Please enter a valid email address."})

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    """Represents a customer order."""

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order #{self.id} - {self.customer.name}"


class OrderItem(models.Model):
    """Represents a single line item within an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_subtotal(self) -> Decimal:
        """Return the subtotal for this line item."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.product.name} x{self.quantity}"
