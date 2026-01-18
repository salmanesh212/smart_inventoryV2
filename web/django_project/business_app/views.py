#Done by BoyWonder
from django import views
from django.shortcuts import render
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
            name = request.POST.get('name')
            category = request.POST.get('category')
            try:
                price = float(request.POST.get('price'))
            except ValueError:
                raise ValueError("Price must be a number.")
            product = Product(name=name, category=category, price=price)
            product.save()
            orderItem=OrderItem(product=product,quantity=0)
            orderItem.save()
            return render(request, 'product_created.html', {'product': product})
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



