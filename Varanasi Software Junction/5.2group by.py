import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

sql = """
SELECT
  c.customer_id,
  c.name,
  SUM(o.amount) AS total_spend,
  COUNT(*) AS orders_count
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC;
"""

df = pd.read_sql(sql, engine)
print(df)