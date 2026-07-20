import pandas as pd
from database.connection import get_engine


engine = get_engine()


def low_stock_products():

    query = """

    SELECT
        p.ProductName,
        i.StockQuantity

    FROM Inventory i

    JOIN Products p
    ON i.ProductID = p.ProductID

    WHERE i.StockQuantity < 20

    ORDER BY i.StockQuantity ASC

    """

    df = pd.read_sql(query, engine)

    print("\nLow Stock Products")
    print(df)

    return df



def inventory_value():

    query = """

    SELECT
        SUM(i.StockQuantity * p.Price) AS InventoryValue

    FROM Inventory i

    JOIN Products p
    ON i.ProductID = p.ProductID

    """

    df = pd.read_sql(query, engine)

    print("\nInventory Value")
    print(df)

    return df



if __name__ == "__main__":
    low_stock_products()
    inventory_value()