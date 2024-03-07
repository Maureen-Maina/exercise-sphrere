from datetime import datetime

class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date

    def calculate_value(self):
        remaining_days = (self.expiry_date - datetime.now()).days
        if remaining_days >= 0:
            discount = remaining_days / 30  # assuming expiry_date is within 30 days
            return self.quantity_in_stock * self.unit_price * (1 - discount)
        else:
            return 0  # product has expired

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

# Example usage:
simple_product = SimpleProduct("001", "Book", 10, 15)
print("Simple Product value:", simple_product.calculate_value())

expiry_date = datetime.now().replace(year=2024, month=4, day=1)  # Assuming May 1, 2024
perishable_product = PerishableProduct("002", "Juice", 20, 2, expiry_date)
print("Perishable Product value:", perishable_product.calculate_value())

digital_product = DigitalProduct("003", "Music Album", 5, 10)
print("Digital Product value:", digital_product.calculate_value())
    
