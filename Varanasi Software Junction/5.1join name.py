import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

sql = """
SELECT
  o.order_id,
  c.name,
  c.city,
  o.amount,
  o.created_at
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.created_at;
"""

df = pd.read_sql(sql, engine)
print(df)