class Product:
    def init(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class InvoiceItem:
    def init(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Invoice:
    def init(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total

# Sample Products
product1 = Product(1, "Laptop", 1000)
product2 = Product(2, "Mouse", 20)
product3 = Product(3, "Keyboard", 50)

# Sample Invoice Items
item1 = InvoiceItem(product1, 2)
item2 = InvoiceItem(product2, 5)
item3 = InvoiceItem(product3, 1)

# Create an Invoice
invoice = Invoice()
invoice.add_item(item1)
invoice.add_item(item2)
invoice.add_item(item3)

# Calculate Total
total_amount = invoice.calculate_total()

# Display Invoice Details
print("Invoice Details:")
for item in invoice.items:
    print(f"{item.product.name} - Quantity: {item.quantity}")

print(f"\nTotal Amount: ${total_amount}")
