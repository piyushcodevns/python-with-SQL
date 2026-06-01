import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/piyush")
df = pd.read_sql("SELECT * FROM info", engine)

df.to_excel("infomation.xlsx", index=False)
print(type(df))
