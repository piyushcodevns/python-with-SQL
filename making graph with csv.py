import pandas as pd
import matplotlib.pyplot as plt
def read_csv():
    df = pd.read_csv("account.csv", index_col=0)
    return df
def getBalance(id, df):
    return df.loc[id, "balance"]
df = read_csv()
print(df)

days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
account_ids = df.index.tolist()[:7]
balance = [getBalance(i, df) for i in account_ids]
plt.plot(days, balance, marker="o")
plt.xlabel("Days")
plt.ylabel("Balance")
plt.title("Weekly Balance Data")
plt.show()
x = getBalance(account_ids[1], df)
print("balance", x)
