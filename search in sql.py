import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:@127.0.0.1:3306/piyush")
df=pd.read_sql("Select * from market",engine)
df.to_csv()