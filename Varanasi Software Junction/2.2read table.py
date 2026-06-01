import sqlite3
import pandas as pd

con = sqlite3.connect("shop.db")
df_customers = pd.read_sql("SELECT * FROM customers;", con)
df_orders = pd.read_sql("SELECT * FROM orders;", con)
con.close()

print(df_customers)
print(df_orders)