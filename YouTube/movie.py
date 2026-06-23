import pandas as pd

df = pd.read_excel("movie.xlsx")

df.to_csv("clean.csv", index=False)

print(df)

