from faker import Faker
import random

fake = Faker()

DEPARTMENTS = [
    "Sales",
    "Marketing",
    "Finance",
    "HR",
    "IT",
    "Operations"
]

JOB_TITLES = [
    "Sales Manager",
    "Sales Executive",
    "Data Analyst",
    "HR Executive",
    "IT Support",
    "Finance Officer",
    "Operations Manager"
]

def generate_employees(n=25):
    employees = []

    for _ in range(n):
        employees.append({
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "Email": fake.unique.email(),
            "Department": random.choice(DEPARTMENTS),
            "JobTitle": random.choice(JOB_TITLES),
            "HireDate": fake.date_between(start_date="-10y", end_date="today"),
            "Salary": round(random.uniform(30000, 120000), 2)
        })

    return employees


if __name__ == "__main__":
    for employee in generate_employees(5):
        print(employee)