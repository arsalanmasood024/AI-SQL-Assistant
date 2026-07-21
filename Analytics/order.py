import pandas as pd
from database.connection import get_engine

engine = get_engine()


def order_status():

    query = """
        SELECT

            Status,

            COUNT(*) AS TotalOrders

        FROM Orders

        GROUP BY Status

        ORDER BY TotalOrders DESC;
        """

    df = pd.read_sql(query, engine)

    print("\nOrders by Status")
    print(df)

    return df


if __name__ == "__main__":
    order_status()