import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

df_more = pd.DataFrame({
  "name": ["Sonia"],
  "city": ["Delhi"]
})

df_more.to_sql("new_customers", engine, if_exists="append", index=False)

print(pd.read_sql("SELECT * FROM new_customers;", engine))