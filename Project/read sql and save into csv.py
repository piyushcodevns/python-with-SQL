import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:@127.0.0.1:3306/piyush")
df=pd.read_sql("SELECT * FROM `customer`", engine)
person_name=input("Enter the name:")
person_data=df[df["Name"]==person_name]
person_data.to_csv(f"{person_name}.csv",index=False)
print(df)
