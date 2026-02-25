"""Django management command to populate sample data for the Smart Inventory System."""

from django.core.management.base import BaseCommand
from business_app.models import Product, Customer, Order, OrderItem
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample products, customers, and orders'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data population...'))

        # Clear existing data (optional)
        # Product.objects.all().delete()
        # Customer.objects.all().delete()
        # Order.objects.all().delete()
        # OrderItem.objects.all().delete()

        # Create Sample Products
        products_data = [
            {'name': 'Laptop Pro 15', 'category': 'Electronics', 'price': 1299.99, 'quantity_in_stock': 25},
            {'name': 'Wireless Mouse', 'category': 'Electronics', 'price': 29.99, 'quantity_in_stock': 150},
            {'name': 'Office Chair', 'category': 'Furniture', 'price': 349.99, 'quantity_in_stock': 40},
            {'name': 'Standing Desk', 'category': 'Furniture', 'price': 599.99, 'quantity_in_stock': 15},
            {'name': 'USB-C Hub', 'category': 'Electronics', 'price': 49.99, 'quantity_in_stock': 200},
            {'name': 'Mechanical Keyboard', 'category': 'Electronics', 'price': 89.99, 'quantity_in_stock': 75},
            {'name': 'Monitor 27"', 'category': 'Electronics', 'price': 399.99, 'quantity_in_stock': 30},
            {'name': 'Desk Lamp', 'category': 'Furniture', 'price': 24.99, 'quantity_in_stock': 100},
            {'name': 'Webcam HD', 'category': 'Electronics', 'price': 59.99, 'quantity_in_stock': 60},
            {'name': 'Notebook Pack (3)', 'category': 'Stationery', 'price': 9.99, 'quantity_in_stock': 300},
        ]

        products = {}
        for data in products_data:
            product, created = Product.objects.get_or_create(
                name=data['name'],
                defaults={
                    'category': data['category'],
                    'price': data['price'],
                    'quantity_in_stock': data['quantity_in_stock'],
                }
            )
            products[data['name']] = product
            if created:
                self.stdout.write(self.style.SUCCESS(f"✓ Created product: {data['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"~ Product already exists: {data['name']}"))

        # Create Sample Customers
        customers_data = [
            {'name': 'Alice Martin', 'email': 'alice.martin@email.com'},
            {'name': 'Bob Johnson', 'email': 'bob.johnson@email.com'},
            {'name': 'Carol Williams', 'email': 'carol.williams@email.com'},
            {'name': 'David Brown', 'email': 'david.brown@email.com'},
            {'name': 'Eve Davis', 'email': 'eve.davis@email.com'},
        ]

        customers = {}
        for data in customers_data:
            customer, created = Customer.objects.get_or_create(
                email=data['email'],
                defaults={'name': data['name']}
            )
            customers[data['name']] = customer
            if created:
                self.stdout.write(self.style.SUCCESS(f"✓ Created customer: {data['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"~ Customer already exists: {data['name']}"))

        # Create Sample Orders
        orders_data = [
            {'customer': 'Alice Martin', 'days_ago': 40, 'items': [
                ('Laptop Pro 15', 1),
                ('Wireless Mouse', 2),
            ]},
            {'customer': 'Bob Johnson', 'days_ago': 35, 'items': [
                ('Office Chair', 1),
                ('Mechanical Keyboard', 1),
            ]},
            {'customer': 'Alice Martin', 'days_ago': 20, 'items': [
                ('USB-C Hub', 3),
                ('Monitor 27"', 1),
            ]},
            {'customer': 'Carol Williams', 'days_ago': 11, 'items': [
                ('Standing Desk', 1),
                ('Desk Lamp', 2),
            ]},
            {'customer': 'David Brown', 'days_ago': -4, 'items': [
                ('Webcam HD', 1),
                ('Notebook Pack (3)', 5),
            ]},
            {'customer': 'Eve Davis', 'days_ago': -15, 'items': [
                ('Laptop Pro 15', 1),
                ('Mechanical Keyboard', 2),
            ]},
        ]

        order_count = 0
        for order_data in orders_data:
            customer = customers[order_data['customer']]
            order_date = datetime.now().date() - timedelta(days=order_data['days_ago'])
            order, created = Order.objects.get_or_create(
                customer=customer,
                order_date=order_date,
            )
            if created:
                order_count += 1
                for product_name, qty in order_data['items']:
                    product = products[product_name]
                    OrderItem.objects.create(order=order, product=product, quantity=qty)
                self.stdout.write(self.style.SUCCESS(f"✓ Created order #{order.id} for {order_data['customer']}"))

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Data population complete!\n'
            f'   - {len(products)} products loaded\n'
            f'   - {len(customers)} customers registered\n'
            f'   - {order_count} orders created'
        ))
