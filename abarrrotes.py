#Proyecto hecho por Salvador, Israel y Francisco

class Product:
    def __init__(self, id, name, price, stock, category, description, supplier):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock
        self._category = category
        self._description = description
        self._supplier = supplier

    def show_info(self):
        info = f"ID: {self._id}\nName: {self._name}\nPrice: {self._price}\nStock: {self._stock}\nCategory: {self._category}\nDescription: {self._description}\nSupplier: {self._supplier}"
        return info

    # Getters
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def get_category(self):
        return self._category

    def get_description(self):
        return self._description

    def get_supplier(self):
        return self._supplier

    # Setters
    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_stock(self, stock):
        self._stock = stock

    def set_category(self, category):
        self._category = category

    def set_description(self, description):
        self._description = description

    def set_supplier(self, supplier):
        self._supplier = supplier

class Store:
    def __init__(self):
        self.name = "Tienda de abarrotes"
        self.products = []
        self.sales = []
        self.totalSales = 0

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product._id != product_id]

    def show_products(self):
        for product in self.products:
            print(product.show_info())
    

class Sale:
    def __init__(self, id, dateTime, products, totalPrice, employee):
        self.id = id
        self.dateTime = dateTime
        self.products = products
        self.totalPrice = totalPrice
        self.employee = employee

    def calculate_total(self):
        self.totalPrice = sum(product._price for product in self.products)
        return self.totalPrice

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def update_balance(self, amount):
        self.balance += amount

    def display_balance(self):
        return f"The current balance is: ${self.balance}"