from sqlalchemy import text
from database.connection import get_engine
from database.data_gen.customer_generator import generate_customers
from database.data_gen.product_generator import generate_products
from database.data_gen.supplier_generator import generate_suppliers
from database.data_gen.category_generator import generate_categories
from database.data_gen.employee_generator import generate_employees
from database.data_gen.order_generator import generate_orders
from database.data_gen.orderitem_generator import generate_order_items
from database.data_gen.inventory_generator import generate_inventory    



engine = get_engine()

customers = generate_customers(100)
categories = generate_categories()
products = generate_products(100)
suppliers = generate_suppliers(30)
employees = generate_employees(25)
orders = generate_orders(list(range(1, 101)), list(range(1, 26)), 200)
order_items = generate_order_items(list(range(1, 201)), list(range(1, 101)), 500)
inventory = generate_inventory(list(range(1, 101)))

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

    customer_ids = [
        row[0] for row in conn.execute(
            text("SELECT CustomerID FROM Customers")
        )
    ]

    employee_ids = [
        row[0] for row in conn.execute(
            text("SELECT EmployeeID FROM Employees")
        )
    ]

    product_ids = [
        row[0] for row in conn.execute(
            text("SELECT ProductID FROM Products")
        )
    ]


    print("✅ IDs fetched successfully!")


    orders = generate_orders(
        customer_ids,
        employee_ids,
        200
    )

  
    for order in orders:

        conn.execute(
            text("""
                INSERT INTO Orders
                (
                    CustomerID,
                    EmployeeID,
                    OrderDate,
                    Status,
                    TotalAmount
                )
                VALUES
                (
                    :CustomerID,
                    :EmployeeID,
                    :OrderDate,
                    :Status,
                    :TotalAmount
                )
            """),
            order
        )


    print("✅ Orders inserted successfully!")


    order_ids = [
        row[0] for row in conn.execute(
            text("SELECT OrderID FROM Orders")
        )
    ]

    order_items = generate_order_items(
        order_ids,
        product_ids,
        500
    )


    for item in order_items:

        conn.execute(
            text("""
                INSERT INTO OrderItems
                (
                    OrderID,
                    ProductID,
                    Quantity,
                    UnitPrice,
                    Discount
                )
                VALUES
                (
                    :OrderID,
                    :ProductID,
                    :Quantity,
                    :UnitPrice,
                    :Discount
                )
            """),
            item
        )


    print("✅ Order Items inserted successfully!")




    inventory = generate_inventory(
        product_ids
    )


    for stock in inventory:

        conn.execute(
            text("""
                INSERT INTO Inventory
                (
                    ProductID,
                    StockQuantity,
                    ReorderLevel,
                    Warehouse,
                    LastUpdated
                )
                VALUES
                (
                    :ProductID,
                    :StockQuantity,
                    :ReorderLevel,
                    :Warehouse,
                    :LastUpdated
                )
            """),
            stock
        )


    print("✅ Inventory inserted successfully!")