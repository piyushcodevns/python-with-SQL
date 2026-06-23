import pandas as pd
from pathlib import Path
input_file = Path("movie.xlsx")
output_file = Path("clean.csv")
df = pd.read_excel(input_file)
df = df.drop_duplicates()
numeric_columns = ["views", "likes", "dislikes", "comment"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=numeric_columns)
print(df.head())
input("Head")
df.info()
df.describe()
df.tail()
df.to_csv(output_file, index=False)
print(df)
print("Saved cleaned file as clean.csv")