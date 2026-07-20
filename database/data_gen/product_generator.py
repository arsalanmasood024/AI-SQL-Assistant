from faker import Faker
import random

fake = Faker()

PRODUCT_NAMES = [
    "Laptop", "Keyboard", "Mouse", "Monitor", "Chair",
    "Desk", "Headphones", "Printer", "Smartphone", "Tablet",
    "Backpack", "Camera", "Speaker", "Watch", "Microphone",
    "Router", "SSD", "Power Bank", "Coffee Maker", "Fan"
]

def generate_products(n=100, max_category_id=20, max_supplier_id=30):
    products = []

    for _ in range(n):
        cost = round(random.uniform(10, 500), 2)
        price = round(cost * random.uniform(1.2, 2.0), 2)

        products.append({
            "ProductName": random.choice(PRODUCT_NAMES),
            "ProductDescription": fake.sentence(nb_words=8),
            "CategoryID": random.randint(1, max_category_id),
            "SupplierID": random.randint(1, max_supplier_id),
            "UnitCost": cost,
            "UnitPrice": price,
            "StockQuantity": random.randint(10, 500)
        })

    return products


if __name__ == "__main__":
    for product in generate_products(5):
        print(product)