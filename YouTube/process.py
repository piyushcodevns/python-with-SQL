import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

input_file = Path("clean.csv")
df = pd.read_csv(input_file)
df = df[["vidid", "views", "likes", "dislikes"]]
print(df)
views = df["views"]
likes = df["likes"]
dislikes = df["dislikes"]
n = len(views)
print(n)
x = [i + 1 for i in range(n)]
model = np.polynomial.Polynomial.fit(views, likes, 2)
coeff = r2_score(likes, model(views))
print(coeff)
plt.plot(views, likes)
plt.plot(x, model(x))
plt.grid(True)
plt.legend()
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Views, likes and dislikes")
plt.show()
