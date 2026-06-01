import sqlite3
import pandas as pd
con = sqlite3.connect("shop.db")
sql = """
SELECT order_id, customer_id, amount, created_at
FROM orders
WHERE amount >= 500
ORDER BY amount DESC;
"""
df = pd.read_sql(sql, con)
con.close()
print(df)