import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@HOST:3306/piyush")
USERNAME = "root"
PASSWORD = ""
HOST = "127.0.0.1"
PORT = 3306 
DATABASE_NAME = "piyush"
database_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
engine = create_engine(database_url)
print(engine)
df = pd.read_sql("SELECT * FROM school;", engine)
print(df)
