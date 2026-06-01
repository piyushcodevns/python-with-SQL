import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

sql = """
SELECT
  o.order_id,
  o.customer_id,
  o.amount,
  o.created_at,
  SUM(o.amount) OVER (
    PARTITION BY o.customer_id
    ORDER BY o.created_at
  ) AS running_total
FROM orders o
ORDER BY o.customer_id, o.created_at;
"""

df = pd.read_sql(sql, engine)
print(df)