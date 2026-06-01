import pandas as pd
import matplotlib.pyplot as plt
def readfromexcel():
    df = pd.read_excel("D:\\bank.xlsx", index_col=0)
    return df
def getBalance(id, df):
    return df.loc[id, "balance"]
df = readfromexcel()
print(df)
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
account_ids = df.index.tolist()[:7]
balances = [getBalance(i, df) for i in account_ids]
plt.plot(account_ids, balances, marker="o")
plt.xlabel("Account ID")
plt.ylabel("Balance")
plt.title("Account Balance Graph")
plt.show()
x = getBalance(account_ids[1], df)
print("balance =", x)
