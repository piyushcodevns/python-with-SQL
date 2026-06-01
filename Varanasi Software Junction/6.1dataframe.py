import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

df_new = pd.DataFrame({
  "name": ["Irfan", "Meera"],
  "city": ["Pune", "Varanasi"]
})

# if_exists:
# 'fail' (default) = error if table exists
# 'replace' = drop + recreate
# 'append' = add rows
df_new.to_sql("new_customers", engine, if_exists="replace", index=False)

# Verify
df_check = pd.read_sql("SELECT * FROM new_customers;", engine)
print(df_check)