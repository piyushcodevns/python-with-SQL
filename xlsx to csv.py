import pandas as pd

df = pd.read_excel("bank.xlsx")  # Load
df.to_csv("account.csv", index=False)  # Save
print(df)
