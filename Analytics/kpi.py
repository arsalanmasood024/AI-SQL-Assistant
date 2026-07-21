import pandas as pd
from database.connection import get_engine

engine = get_engine()


def dashboard_kpis():

    query = """
    SELECT

        COUNT(*) AS TotalOrders,

        SUM(TotalAmount) AS TotalRevenue,

        AVG(TotalAmount) AS AverageOrderValue,

        COUNT(DISTINCT CustomerID) AS TotalCustomers

    FROM Orders;
    """

    df = pd.read_sql(query, engine)

    print("\nDashboard KPIs")
    print(df)

    return df


if __name__ == "__main__":
    dashboard_kpis()