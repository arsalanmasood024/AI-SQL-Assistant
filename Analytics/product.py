import pandas as pd
from database.connection import get_engine

engine = get_engine()


def top_products():

    query = """
    SELECT TOP 10
        p.ProductName,
        SUM(oi.Quantity) AS UnitsSold,
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue
    FROM OrderItems oi
    JOIN Products p
        ON oi.ProductID = p.ProductID
    GROUP BY p.ProductName
    ORDER BY UnitsSold DESC;
    """

    df = pd.read_sql(query, engine)

    print("\nTop Selling Products")
    print(df)

    return df


def category_sales():

    query = """
    SELECT
        c.CategoryName,
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue
    FROM OrderItems oi
    JOIN Products p
        ON oi.ProductID = p.ProductID
    JOIN Categories c
        ON p.CategoryID = c.CategoryID
    GROUP BY c.CategoryName
    ORDER BY Revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\nCategory Revenue")
    print(df)

    return df

def product_revenue():

    query = """

    SELECT

        p.ProductName,

        SUM(oi.Quantity * oi.UnitPrice) AS Revenue

    FROM OrderItems oi

    JOIN Products p
        ON oi.ProductID=p.ProductID

    GROUP BY p.ProductName

    ORDER BY Revenue DESC;

    """

    df = pd.read_sql(query, engine)

    print("\nProduct Revenue")
    print(df)

    return df

if __name__ == "__main__":
    top_products()
    category_sales()