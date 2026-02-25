"""Django forms with validation for the Smart Inventory System."""

from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Customer, Order, OrderItem


class ProductForm(forms.ModelForm):
    """Form for creating and updating products."""

    class Meta:
        model = Product
        fields = ['name', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'E.g. Latitude 7440',
                'id': 'name',
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'E.g. Electronics',
                'id': 'category',
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '1299.00',
                'step': '0.01',
                'id': 'price',
            }),
        }

    def clean_price(self) -> float:
        """Validate that price is greater than zero."""
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price

    def clean_name(self) -> str:
        """Validate that name is not empty."""
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise ValidationError("Product name is required.")
        return name


class CustomerForm(forms.ModelForm):
    """Form for registering customers with email validation."""

    class Meta:
        model = Customer
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Jordan Williams',
                'id': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'jordan@client.io',
                'id': 'email',
            }),
        }

    def clean_email(self) -> str:
        """Validate that the email is properly formatted and unique."""
        email = self.cleaned_data.get('email', '').strip()
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValidationError("Please enter a valid email address.")
        if Customer.objects.filter(email=email).exists():
            if not self.instance.pk or self.instance.email != email:
                raise ValidationError("A customer with this email already exists.")
        return email


class OrderForm(forms.Form):
    """Form for creating orders."""

    customer_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'E.g. 1, 2, 3...',
            'id': 'customer_id',
            'min': '1',
        }),
    )
    product_id = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'product_id'}),
    )
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'E.g. 1, 2, 3...',
            'id': 'quantity',
            'min': '1',
            'value': '1',
        }),
    )

    def clean_quantity(self) -> int:
        """Validate that quantity is a positive number."""
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity <= 0:
            raise ValidationError("Quantity must be a positive number.")
        return quantity
