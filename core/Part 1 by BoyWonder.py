#Part 1 by BoyWonder

#First Class:product
class Product:
    def __init__(self, id, name, category, price,quantity_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.qis=quantity_in_stock
    
    def add_stock(self,qty):
        self.qis+=qty
        print("Stock is added succesfuly")
    
    def remove_stock(self,qty):
        self.qis-=qty
        if self.qis <= 0: 
            raise ValueError("Quantity must be positive")
        else:
            print("Stock is removed succesfuly")

    def get_value_in_stock(self):
        return self.qis
    
#Second Class:Customer
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    def validate_email(self):
        if "@gmail.com" not in self.email:
            raise ValueError("Invalid Email")
        else:
            print("Correct email")

   
#Third Class :OrderItem
class OrderItem:
    def __init__(self,prod,quantity):
        self.product=prod
        self.quantity=quantity
        self.product=Product(prod.id,prod.name,prod.category,prod.price,prod.qis)
    
    def get_subtotal(self):
        return self.product.price*self.quantity
    
#Fourth Class:Order
class Order:
    def __init__(self, id, customer, order_date,items):
        self.items=[OrderItem(items.product,items.quantity)]
        self.id = id
        self.customer=customer
        self.od=order_date
        

    def add_item(self,prod,quant):
        self.items[-1].product,self.items[-1].quantity=prod,quant
        if prod is self.items[-1].product and quant is self.items[-1].quantity:
            print("Item is added succesfuly")

        else:
            print("Item is not added,please try it again")
    
    def calculate_total(self):
        s=0
        for x in self.items:
            s+=(x.product.price*x.quantity)
        return s#Part 1 by BoyWonder

#First Class:product
class Product:
    def __init__(self, id, name, category, price,quantity_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.qis=quantity_in_stock
    
    def add_stock(self,qty):
        self.qis+=qty
        print("Stock is added succesfuly")
    
    def remove_stock(self,qty):
        self.qis-=qty
        if self.qis <= 0: 
            raise ValueError("Quantity must be positive")
        else:
            print("Stock is removed succesfuly")

    def get_value_in_stock(self):
        return self.qis
    
#Second Class:Customer
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    def validate_email(self):
        if "@gmail.com" not in self.email:
            raise ValueError("Invalid Email")
        else:
            print("Correct email")

   
#Third Class :OrderItem
class OrderItem:
    def __init__(self,prod,quantity):
        self.product=prod
        self.quantity=quantity
        self.product=Product(prod.id,prod.name,prod.category,prod.price,prod.qis)
    
    def get_subtotal(self):
        return self.product.price*self.quantity
    
#Fourth Class:Order
class Order:
    def __init__(self, id, customer, order_date,items):
        self.items=[OrderItem(items.product,items.quantity)]
        self.id = id
        self.customer=customer
        self.od=order_date
        

    def add_item(self,prod,quant):
        self.items[-1].product,self.items[-1].quantity=prod,quant
        if prod is self.items[-1].product and quant is self.items[-1].quantity:
            print("Item is added succesfuly")

        else:
            print("Item is not added,please try it again")
    
    def calculate_total(self):
        s=0
        for x in self.items:
            s+=(x.product.price*x.quantity)
        return s
    
#Test all classes functions
if __name__ == "__main__":
    p1 = Product(1, "Laptop", "Electronics", 1500.0, 10)
    p2 = Product(2, "Smartphone", "Electronics", 800.0, 20)
    p1.add_stock(5)
    p2.remove_stock(3)
    p1.get_value_in_stock()

    oi1 = OrderItem(p1, 2)
    mm=oi1.get_subtotal()
    print(f"Subtotal for order item: {mm}")

    c1 = Customer(1, "Alice", "alice@gmail.com")
    c2 = Customer(2, "Bob", "bob@gmail.com")
    c1.validate_email()
    c2.validate_email()


    order = Order(1, c2, "2023-10-01", oi1)
    order.add_item(p2, 1)
    total = order.calculate_total()
    print(f"Total order amount: {total}")
    print(f"Product 1 stock value: {p1.get_value_in_stock()}")


        




