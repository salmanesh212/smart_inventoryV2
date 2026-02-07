from django.db import models    #Création des modèles de la base de données(des classes)
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)#2 chiffres après la virgule, 10 chiffres au total

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)#Clé étrangére,meme definition que SQL
    quantity=models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    items = models.ManyToManyField(OrderItem) # Association entre une commande et ses articles(définit qu'un ordre peut contenir plusieurs articles et qu'un article peut appartenir à plusieurs ordres)


# Create your models here.
