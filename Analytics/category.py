import pandas as pd
from database.connection import get_engine

engine = get_engine()


def category_sales():

    query = """
    SELECT
        c.CategoryName,
        SUM(oi.Quantity * oi.UnitPrice) AS Revenue,
        SUM(oi.Quantity) AS UnitsSold

    FROM OrderItems oi

    JOIN Products p
        ON oi.ProductID = p.ProductID

    JOIN Categories c
        ON p.CategoryID = c.CategoryID

    GROUP BY c.CategoryName

    ORDER BY Revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\nSales by Category")
    print(df)

    return df


if __name__ == "__main__":
    category_sales()