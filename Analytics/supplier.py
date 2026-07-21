import pandas as pd
from database.connection import get_engine

engine = get_engine()


def supplier_sales():

    query = """

    SELECT

        s.SupplierName,

        SUM(oi.Quantity * oi.UnitPrice) AS Revenue,

        SUM(oi.Quantity) AS UnitsSold

    FROM OrderItems oi

    JOIN Products p
        ON oi.ProductID = p.ProductID

    JOIN Suppliers s
        ON p.SupplierID = s.SupplierID

    GROUP BY s.SupplierName

    ORDER BY Revenue DESC;

    """

    df = pd.read_sql(query, engine)

    print("\nSupplier Performance")
    print(df)

    return df


if __name__ == "__main__":
    supplier_sales()