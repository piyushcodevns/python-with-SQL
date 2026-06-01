import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")
df = pd.read_sql("SELECT * FROM customers;", engine)
print(df)