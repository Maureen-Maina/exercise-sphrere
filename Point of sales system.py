class SaleItem:
    def __init__(self, item_id, name, unit_price):
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price

    def calculate_total(self, quantity):
        pass

class StandardItem(SaleItem):
    def __init__(self, item_id, name, unit_price):
        super().__init__(item_id, name, unit_price)

    def calculate_total(self, quantity):
        return self.unit_price * quantity

class DiscountedItem(SaleItem):
    def __init__(self, item_id, name, unit_price, discount_percentage):
        super().__init__(item_id, name, unit_price)
        self.discount_percentage = discount_percentage

    def calculate_total(self, quantity):
        discounted_price = self.unit_price * (1 - self.discount_percentage / 100)
        return discounted_price * quantity

class ServiceItem(SaleItem):
    def __init__(self, item_id, name, hourly_rate):
        super().__init__(item_id, name, hourly_rate)

    def calculate_total(self, hours):
        return self.unit_price * hours

# Example usage:
standard_item = StandardItem("001", "Product A", 20)
print("Total cost for 5 units of Standard Item:", standard_item.calculate_total(5))

discounted_item = DiscountedItem("002", "Product B", 30, 20)
print("Total cost for 3 units of Discounted Item:", discounted_item.calculate_total(3))

service_item = ServiceItem("003", "Consulting", 70)
print("Total cost for 2 hours of Service Item:", service_item.calculate_total(2))
