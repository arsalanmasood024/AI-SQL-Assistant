import pandas as pd
from sqlalchemy import text
from database.connection import get_engine


def total_revenue():

    engine = get_engine()

    query = """
    SELECT 
        SUM(TotalAmount) AS TotalRevenue
    FROM Orders
    """

    df = pd.read_sql(query, engine)

    print("\nTotal Revenue")
    print(df)


def monthly_sales():

    engine = get_engine()

    query = """
    SELECT
        MONTH(OrderDate) AS Month,
        SUM(TotalAmount) AS Revenue
    FROM Orders
    GROUP BY MONTH(OrderDate)
    ORDER BY Month
    """

    df = pd.read_sql(query, engine)

    print("\nMonthly Sales")
    print(df)

    df.plot(
        x="Month",
        y="Revenue",
        kind="line",
        marker="o",
        title="Monthly Revenue Trend"
    )

    import matplotlib.pyplot as plt
    plt.show()


def top_products():

    engine = get_engine()

    query = """
    SELECT TOP 10
        p.ProductName,
        SUM(oi.Quantity) AS UnitsSold
    FROM OrderItems oi
    JOIN Products p
    ON oi.ProductID = p.ProductID
    GROUP BY p.ProductName
    ORDER BY UnitsSold DESC
    """

    df = pd.read_sql(query, engine)

    print("\nTop Selling Products")
    print(df)

def product_revenue():

    engine = get_engine()

    query = """
    SELECT TOP 10
        p.ProductName,
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue
    FROM OrderItems oi
    JOIN Products p
    ON oi.ProductID = p.ProductID
    GROUP BY p.ProductName
    ORDER BY Revenue DESC
    """

    df = pd.read_sql(query, engine)

    print("\nTop Revenue Products")
    print(df)




if __name__ == "__main__":

    total_revenue()

    monthly_sales()

    top_products()

    product_revenue()