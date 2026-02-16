#part 2 by BoyWonder
import mysql.connector

class ProductDAO:
    def __init__(self, id, name, category, price,quantity_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.qis=quantity_in_stock
    def save(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Products (product_id,last_name,category,price,quantity_in_stock) VALUES (%s, %s, %s, %s, %s) ",(self.id,self.name,self.category,self.price,self.qis))
            conn.commit()
            print("Product saved successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée") 
                  
    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Products SET last_name=%s, category=%s, price=%s, quantity_in_stock=%s WHERE product_id=%s",(self.name,self.category,self.price,self.qis,self.id))
            conn.commit()
            print("Product updated successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée") 
    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE * FROM Products WHERE product_id=%s",(self.id,))
            conn.commit()
            print("Product deleted successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée") 

    def find_by_id(self,conn,id):
        cursor=conn.cursor
        try:
            cursor.execute("SELECT * FROM Products WHERE product_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except:
            conn.rollback() 
            print("Erreur — ID non trouvée!") 

class CustomerDAO:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    def save(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Customer (customer_id,last_name,email) VALUES (%s, %s, %s) ",(self.id,self.name,self.email))
            conn.commit()
            print("Customer saved successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée") 
    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Customer SET name=%s, email=%s WHERE customer_id=%s",(self.name,self.email,self.id))
            conn.commit()
            print("Customer updated successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée")
    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE * FROM Customer WHERE customer_id=%s",(self.id,))
            conn.commit()
            print("Customer deleted successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée")
    def find_by_id(self,conn,id):
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM Customer WHERE customer_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except:
            conn.rollback() 
            print("Erreur — ID non trouvée!")

class OrderDAO:
    def __init__(self,id,customer_id,order_date,orderitem_id):
        self.id=id
        self.customer_id=customer_id
        self.order_date=order_date
        self.orderitem_id=orderitem_id
    def save(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Order (order_id,customer_id,order_date,orderitem_id) VALUES (%s, %s, %s,%s) ",(self.id,self.customer_id,self.order_date,self.orderitem_id))
            conn.commit()
            print("Order saved successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée") 
    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Order SET customer_id=%s, order_date=%s, orderitem_id=%s WHERE order_id=%s",(self.customer_id,self.order_date,self.orderitem_id,self.id))
            conn.commit()
            print("Order updated successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée")
    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE * FROM Order WHERE order_id=%s",(self.id,))
            conn.commit()
            print("Order deleted successfully")
        except:
            conn.rollback() 
            print("Erreur — aucune modification appliquée")
    def find_by_id(self,conn,id):
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM Order WHERE order_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except:
            conn.rollback() 
            print("Erreur — ID non trouvée!")




