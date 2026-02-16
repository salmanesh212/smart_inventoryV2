#Done by BoyWonder
from django import views
from django.shortcuts import render
from django.db.models import Sum, Count, F, Avg
from django.db.models.functions import TruncMonth
from .models import Product, Customer, OrderItem, Order

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_Create(request):
    if request.method == 'POST': #POST mean submit data to server
        try:
            name = request.POST.get('name') #Prendre les données du formulaire
            category = request.POST.get('category')
            try:
                price = float(request.POST.get('price'))
            except ValueError:
                raise ValueError("Price must be a number.")
            product = Product(name=name, category=category, price=price)
            product.save()
            orderItem=OrderItem(product=product,quantity=0)
            orderItem.save()
            return render(request, 'product_created.html', {'product': product}) #Render est une fnction qui permet d'afficher une page HTML
        except ValueError:
            print("Price must be a number and greater than zero.")
    return render(request, 'create_product.html')

def product_read(request, product_id):
    if product_id is None:
        return render(request, 'error.html', {'message': 'Product ID is required.'})
    else:
        product = Product.objects.get(id=product_id)
        return render(request, 'product_detail.html', {'product': product})

def product_update(request,NewProductid):
    product = Product.objects.get(id=NewProductid)
    if request.method == 'POST':   #POST mean submit data to server
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.save()
        return render(request, 'product_updated.html', {'product': product})
    return render(request, 'update_product.html', {'product': product})

def product_delete(request, product_id):
    if product_id is None:
        return render(request, 'error.html', {'message': 'Product ID is required.'})
    else:
        product = Product.objects.get(id=product_id)
        product.delete()
        return render(request, 'product_deleted.html')

def customer_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        customer = Customer(name=name, email=email)
        customer.save()
        return render(request, 'customer_registered.html', {'customer': customer})
    return render(request, 'register_customer.html')

def create_order(request):
    products = Product.objects.all()
    if request.method == 'POST':
        try:
            customer_id = request.POST.get('customer_id')
            customer = Customer.objects.get(id=customer_id)
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            quantity = int(request.POST.get('quantity'))
            item = OrderItem(product=product, quantity=quantity)
            item.save()
            order = Order(customer=customer)
            order.save()
            return render(request, 'order_created.html', {'order': order, 'item': item})
        except Customer.DoesNotExist:
            return render(request, 'error.html', {'message': 'Customer not found. Please register the customer first.'})
        except Product.DoesNotExist:
            return render(request, 'error.html', {'message': 'Product not found. Please create the product first.'})
        except ValueError:
            return render(request, 'error.html', {'message': 'Invalid input. Please enter valid numbers.'})
    return render(request, 'create_order.html', {'products': products})

def display_orders(request):
    orders = Order.objects.all()
    return render(request, 'display_orders.html', {'orders': orders})


def analytics_dashboard(request):
    """Dashboard displaying key business analytics using Django ORM (same logic as the pandas notebook)."""

    # --- Revenue per month ---
    revenue_per_month_qs = (
        Order.objects
        .annotate(month=TruncMonth('order_date'))
        .values('month')
        .annotate(revenue=Sum(F('items__quantity') * F('items__product__price')))
        .order_by('month')
    )
    revenue_labels = [entry['month'].strftime('%b %Y') if entry['month'] else 'N/A' for entry in revenue_per_month_qs]
    revenue_data = [float(entry['revenue']) if entry['revenue'] else 0 for entry in revenue_per_month_qs]

    # --- Best-selling products ---
    best_products_qs = (
        OrderItem.objects
        .values(product_name=F('product__name'))
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')
    )
    best_product_labels = [p['product_name'] for p in best_products_qs]
    best_product_data = [p['total_qty'] for p in best_products_qs]

    # --- Total stock value ---
    stock_value = (
        Product.objects
        .aggregate(total=Sum(F('price') * F('id')))  # quantity_in_stock not in Django model, fallback
    )
    # Use raw SQL to get real stock value from the MySQL table which has quantity_in_stock
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT COALESCE(SUM(price * quantity_in_stock), 0) FROM Products")
        total_stock_value = float(cursor.fetchone()[0])

    # --- Average order value ---
    avg_order_qs = (
        Order.objects
        .annotate(order_total=Sum(F('items__quantity') * F('items__product__price')))
        .aggregate(avg_value=Avg('order_total'))
    )
    average_order_value = float(avg_order_qs['avg_value']) if avg_order_qs['avg_value'] else 0

    # --- Purchase frequency per customer ---
    customer_frequency_qs = (
        Order.objects
        .values(customer_name=F('customer__name'))
        .annotate(order_count=Count('id'))
        .order_by('-order_count')
    )

    # --- Summary counts ---
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()

    context = {
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



