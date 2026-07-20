from faker import Faker
import random

fake = Faker()

def generate_customers(n=100):
    customers = []

    for _ in range(n):
        customers.append({
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "Email": fake.unique.email(),
            "Phone": fake.phone_number()[:20],
            "City": fake.city(),
            "Country": fake.country(),
            "RegistrationDate": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        })

    return customers


if __name__ == "__main__":
    data = generate_customers(5)

    for row in data:
        print(row)