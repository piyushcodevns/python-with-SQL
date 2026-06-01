import sqlite3
import pandas as pd

min_amount = 500

con = sqlite3.connect("shop.db")
sql = "SELECT * FROM orders WHERE amount >= ? ORDER BY amount DESC;"
df = pd.read_sql(sql, con, params=(min_amount,))
con.close()

print(df)