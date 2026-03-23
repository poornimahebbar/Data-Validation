import mysql.connector
import pandas as pd

def get_db_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd01",
        database="northwind_db"
    )

    query = """
SELECT 
    p.ProductName,
    a.OrderID,
    a.CustomerID,
    a.EmployeeID,
    a.orderDate,
    a.shipperID,
    b.ProductID,
    (b.Quantity * p.Price) AS priceQuantity
FROM Orders a
JOIN OrderDetails b ON a.OrderID = b.OrderID
JOIN Products p ON b.ProductID = p.ProductID
""";
    df = pd.read_sql(query, conn)
    conn.close()

    return df