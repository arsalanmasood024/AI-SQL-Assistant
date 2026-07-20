from sqlalchemy import text
from database.connection import get_engine
from database.data_gen.customer_generator import generate_customers
from database.data_gen.product_generator import generate_products
from database.data_gen.supplier_generator import generate_suppliers
from database.data_gen.category_generator import generate_categories
from database.data_gen.employee_generator import generate_employees



engine = get_engine()

customers = generate_customers(100)
categories = generate_categories()
products = generate_products(100)
suppliers = generate_suppliers(30)
employees = generate_employees(25)

with engine.begin() as conn:

    for category in categories:
            conn.execute(
                text("""
                    INSERT INTO Categories
                    (CategoryName, Description)
                    VALUES
                    (:CategoryName, :Description)
                """),
                category
            )
    print("✅ Categories inserted successfully!")

    for supplier in suppliers:
        conn.execute(
            text("""
                INSERT INTO Suppliers
                (SupplierName, ContactPerson, Email, Phone, City, Country)
                VALUES
                (:SupplierName, :ContactPerson, :Email, :Phone, :City, :Country)
            """),
            supplier
        )

    print("✅ Suppliers inserted successfully!")

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


    for product in products:
        conn.execute(
            text("""
            INSERT INTO Products
            (
                ProductName,
                ProductDescription,
                CategoryID,
                SupplierID,
                UnitPrice,
                UnitCost,
                StockQuantity
            )
            VALUES
            (
                :ProductName,
                :ProductDescription,
                :CategoryID,
                :SupplierID,
                :UnitPrice,
                :UnitCost,
                :StockQuantity
            )
            """),
            product
        )
    print("✅ Products inserted successfully!")

    for employee in employees:
        conn.execute(
            text("""
                INSERT INTO Employees
                (
                    FirstName,
                    LastName,
                    Email,
                    Department,
                    JobTitle,
                    HireDate,
                    Salary
                )
                VALUES
                (
                    :FirstName,
                    :LastName,
                    :Email,
                    :Department,
                    :JobTitle,
                    :HireDate,
                    :Salary
                )
            """),
            employee
        )

    print("✅ Employees inserted successfully!")