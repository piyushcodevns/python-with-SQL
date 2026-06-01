import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("data.csv")
df.to_excel("data.xlsx",index=False)
print(df)