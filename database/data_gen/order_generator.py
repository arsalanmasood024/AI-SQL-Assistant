from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


def generate_orders(customer_ids, employee_ids, count=200):

    statuses = [
        "Pending",
        "Processing",
        "Shipped",
        "Delivered",
        "Cancelled"
    ]

    orders = []

    for _ in range(count):

        orders.append({

            "CustomerID": random.choice(customer_ids),

            "EmployeeID": random.choice(employee_ids),

            "OrderDate": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),

            "Status": random.choice(statuses),

            "TotalAmount": round(
                random.uniform(50,5000),
                2
            )

        })

    return orders