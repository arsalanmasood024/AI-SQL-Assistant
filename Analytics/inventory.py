import pandas as pd
from database.connection import get_engine

engine = get_engine()


def low_stock():

    query = """

    SELECT

        ProductName,

        StockQuantity

    FROM Products

    WHERE StockQuantity < 10

    ORDER BY StockQuantity;

    """

    df = pd.read_sql(query, engine)

    print("\nLow Stock Products")
    print(df)

    return df


def inventory_value():

    query = """

    SELECT

        SUM(StockQuantity * UnitCost) AS InventoryValue

    FROM Products;

    """

    df = pd.read_sql(query, engine)

    print("\nInventory Value")
    print(df)

    return df


if __name__ == "__main__":
    low_stock()
    inventory_value()