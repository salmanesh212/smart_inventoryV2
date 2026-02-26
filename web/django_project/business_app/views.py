"""Views for the Smart Inventory business application."""

import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Sum, Count, F, Avg
from django.db.models.functions import TruncMonth
from django.core.exceptions import ValidationError

from .models import Product, Customer, OrderItem, Order
from .forms import ProductForm, CustomerForm, OrderForm

logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with quick stats."""
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    low_stock = Product.objects.filter(quantity_in_stock__lte=5).count()
    context = {
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'low_stock': low_stock,
    }
    return render(request, 'index.html', context)


def list_products(request: HttpRequest) -> HttpResponse:
    """Display all products."""
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_Create(request: HttpRequest) -> HttpResponse:
    """Create a new product using ProductForm."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            logger.info("Product '%s' created", product.name)
            return render(request, 'product_created.html', {'product': product})
        else:
            message = "; ".join(
                err for errors in form.errors.values() for err in errors
            )
            logger.warning("Product creation failed: %s", message)
            return render(request, 'error.html', {'message': message})
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def product_read(request: HttpRequest, product_id: int) -> HttpResponse:
    """Display a single product's details."""
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'product_detail.html', {'product': product})
    except Product.DoesNotExist:
        logger.warning("Product #%d not found", product_id)
        return render(request, 'error.html', {'message': 'Product not found.'})


def product_update(request: HttpRequest, NewProductid: int) -> HttpResponse:
    """Update an existing product using ProductForm."""
    try:
        product = Product.objects.get(id=NewProductid)
    except Product.DoesNotExist:
        logger.warning("Product #%d not found for update", NewProductid)
        return render(request, 'error.html', {'message': 'Product not found.'})
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            logger.info("Product '%s' updated", product.name)
            return render(request, 'product_updated.html', {'product': product})
        else:
            message = "; ".join(
                err for errors in form.errors.values() for err in errors
            )
            logger.warning("Product update failed: %s", message)
            return render(request, 'error.html', {'message': message})
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'product': product, 'form': form})


def product_delete(request: HttpRequest, product_id: int) -> HttpResponse:
    """Delete a product by its ID."""
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        logger.info("Product #%d deleted", product_id)
        return render(request, 'product_deleted.html')
    except Product.DoesNotExist:
        logger.warning("Product #%d not found for deletion", product_id)
        return render(request, 'error.html', {'message': 'Product not found.'})


def customer_registration(request: HttpRequest) -> HttpResponse:
    """Register a new customer with email validation using CustomerForm."""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            logger.info("Customer '%s' registered", customer.name)
            return render(request, 'customer_registered.html', {'customer': customer})
        else:
            message = "; ".join(
                err for errors in form.errors.values() for err in errors
            )
            logger.warning("Customer registration failed: %s", message)
            return render(request, 'error.html', {'message': message})
    else:
        form = CustomerForm()
    return render(request, 'register_customer.html', {'form': form})


def create_order(request: HttpRequest) -> HttpResponse:
    """Create a new order with items using OrderForm."""
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                customer = Customer.objects.get(id=form.cleaned_data['customer_id'])
                product = Product.objects.get(id=form.cleaned_data['product_id'])
                quantity = form.cleaned_data['quantity']
                if quantity > product.quantity_in_stock:
                    raise ValueError(
                        f"Not enough stock. Available: {product.quantity_in_stock}, requested: {quantity}"
                    )
                product.quantity_in_stock -= quantity
                product.save()
                order = Order(customer=customer)
                order.save()
                item = OrderItem(order=order, product=product, quantity=quantity)
                item.save()
                logger.info("Order #%d created for customer '%s'", order.id, customer.name)
                return render(request, 'order_created.html', {'order': order})
            except Customer.DoesNotExist:
                logger.warning("Order creation failed: customer not found")
                return render(request, 'error.html', {'message': 'Customer not found. Please register the customer first.'})
            except Product.DoesNotExist:
                logger.warning("Order creation failed: product not found")
                return render(request, 'error.html', {'message': 'Product not found. Please create the product first.'})
            except ValueError as e:
                logger.warning("Order creation failed: %s", e)
                return render(request, 'error.html', {'message': str(e)})
        else:
            message = "; ".join(
                err for errors in form.errors.values() for err in errors
            )
            return render(request, 'error.html', {'message': message})
    return render(request, 'create_order.html', {'products': products})


def display_orders(request: HttpRequest) -> HttpResponse:
    """Display all orders with their items."""
    orders = Order.objects.all().prefetch_related('items__product')
    return render(request, 'display_orders.html', {'orders': orders})


def analytics_dashboard(request: HttpRequest) -> HttpResponse:
    """Render the analytics dashboard with aggregated business data."""
    revenue_per_month_qs = (
        Order.objects
        .annotate(month=TruncMonth('order_date'))
        .values('month')
        .annotate(revenue=Sum(F('items__quantity') * F('items__product__price')))
        .order_by('month')
    )
    revenue_labels: list[str] = [
        entry['month'].strftime('%b %Y') if entry['month'] else 'N/A'
        for entry in revenue_per_month_qs
    ]
    revenue_data: list[float] = [
        float(entry['revenue']) if entry['revenue'] else 0
        for entry in revenue_per_month_qs
    ]

    best_products_qs = (
        OrderItem.objects
        .values(product_name=F('product__name'))
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')
    )
    best_product_labels: list[str] = [p['product_name'] for p in best_products_qs]
    best_product_data: list[int] = [p['total_qty'] for p in best_products_qs]

    stock_value = Product.objects.aggregate(
        total=Sum(F('price') * F('quantity_in_stock'))
    )
    total_stock_value: float = float(stock_value['total']) if stock_value['total'] else 0

    avg_order_qs = (
        Order.objects
        .annotate(order_total=Sum(F('items__quantity') * F('items__product__price')))
        .aggregate(avg_value=Avg('order_total'))
    )
    average_order_value: float = float(avg_order_qs['avg_value']) if avg_order_qs['avg_value'] else 0

    customer_frequency_qs = (
        Order.objects
        .values(customer_name=F('customer__name'))
        .annotate(order_count=Count('id'))
        .order_by('-order_count')
    )

    total_products: int = Product.objects.count()
    total_customers: int = Customer.objects.count()
    total_orders: int = Order.objects.count()

    context: dict = {
        'revenue_labels': revenue_labels,
        'revenue_data': revenue_data,
        'best_product_labels': best_product_labels,
        'best_product_data': best_product_data,
        'total_stock_value': total_stock_value,
        'average_order_value': round(average_order_value, 2),
        'customer_frequency': customer_frequency_qs,
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
    }
    return render(request, 'analytics_dashboard.html', context)



