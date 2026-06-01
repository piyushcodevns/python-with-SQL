import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

sql = "SELECT * FROM orders;"
chunks = pd.read_sql(sql, engine, chunksize=2)

total = 0
rows = 0

for chunk in chunks:
  rows += len(chunk)
  total += chunk["amount"].sum()

print("rows:", rows)
print("total amount:", total)