import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///shop.db")

sql = text("""
SELECT * FROM orders
WHERE amount >= :min_amount
ORDER BY amount DESC
""")

df = pd.read_sql(sql, engine, params={"min_amount": 500})
print(df)