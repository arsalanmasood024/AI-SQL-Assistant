from sqlalchemy import text
from database.connection import get_engine
from database.data_gen.customer_generator import generate_customers

engine = get_engine()

customers = generate_customers(100)

with engine.begin() as conn:
    for customer in customers:
        conn.execute(
            text("""
                INSERT INTO Customers
                (FirstName, LastName, Email, Phone, City, Country, RegistrationDate)
                VALUES
                (:FirstName, :LastName, :Email, :Phone, :City, :Country, :RegistrationDate)
            """),
            customer
        )

print("✅ 100 customers inserted successfully!")