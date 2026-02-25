from core.exceptions import OutOfStockException, InvalidQuantityException


class Product:
    def __init__(self, id, name, category, price, quantity_in_stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def add_stock(self, qty):
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        self.quantity_in_stock += qty
        print("Stock added successfully")

    def remove_stock(self, qty):
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        if qty > self.quantity_in_stock:
            raise OutOfStockException(
                f"Not enough stock. Available: {self.quantity_in_stock}, requested: {qty}"
            )
        self.quantity_in_stock -= qty
        print("Stock removed successfully")

    def get_value_in_stock(self):
        return self.price * self.quantity_in_stock
