import pandas as pd
from database.connection import get_engine


def top_customers():

    engine = get_engine()

    query = """
            SELECT TOP 10
                CONCAT(c.FirstName,' ',c.LastName) AS CustomerName,
                COUNT(o.OrderID) AS TotalOrders,
                SUM(o.TotalAmount) AS TotalSpent
            FROM Customers c
            JOIN Orders o
            ON c.CustomerID = o.CustomerID
            GROUP BY c.FirstName, c.LastName
            ORDER BY TotalSpent DESC
            """

    df = pd.read_sql(query, engine)

    print("\nTop Customers")
    print(df)


def average_order_value():

    engine = get_engine()

    query = """
    SELECT
        AVG(TotalAmount) AS AverageOrderValue
    FROM Orders
    """

    df = pd.read_sql(query, engine)

    print("\nAverage Order Value")
    print(df)


if __name__ == "__main__":

    top_customers()
    average_order_value()