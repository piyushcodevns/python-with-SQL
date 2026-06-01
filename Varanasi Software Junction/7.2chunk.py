import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db")

# Example: add a derived column and store to a new table
chunks = pd.read_sql("SELECT * FROM orders;", engine, chunksize=2)

first = True
for chunk in chunks:
  chunk["amount_with_gst"] = chunk["amount"] * 1.18
  chunk.to_sql("orders_enriched", engine,
               if_exists=("replace" if first else "append"),
               index=False)
  first = False

print(pd.read_sql("SELECT * FROM orders_enriched;", engine))