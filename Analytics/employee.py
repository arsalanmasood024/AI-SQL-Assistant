import pandas as pd
from database.connection import get_engine


engine = get_engine()


def employee_orders():

    query = """

    SELECT TOP 10

        CONCAT(e.FirstName,' ',e.LastName) AS Employee,

        COUNT(o.OrderID) AS TotalOrders,

        SUM(o.TotalAmount) AS Sales


    FROM Orders o

    JOIN Employees e

    ON o.EmployeeID = e.EmployeeID


    GROUP BY
        e.FirstName,
        e.LastName


    ORDER BY Sales DESC

    """


    df = pd.read_sql(query, engine)

    print("\nEmployee Performance")
    print(df)

    return df

def employee_sales():

    query = """

    SELECT

        e.FirstName + ' ' + e.LastName AS Employee,

        SUM(o.TotalAmount) AS Revenue

    FROM Employees e

    JOIN Orders o
        ON e.EmployeeID=o.EmployeeID

    GROUP BY
        e.FirstName,
        e.LastName

    ORDER BY Revenue DESC;

    """

    df = pd.read_sql(query, engine)

    print("\nEmployee Revenue")
    print(df)

    return df

if __name__ == "__main__":
    employee_orders()