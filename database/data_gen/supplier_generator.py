from faker import Faker
import random

fake = Faker()

def generate_suppliers(n=30):
    suppliers = []

    for _ in range(n):
        suppliers.append({
            "SupplierName": fake.company(),
            "ContactPerson": fake.name(),
            "Email": fake.company_email(),
            "Phone": fake.phone_number(),
            "City": fake.city(),
            "Country": fake.country()
        })

    return suppliers


if __name__ == "__main__":
    for supplier in generate_suppliers(5):
        print(supplier)