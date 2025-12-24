import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv("./matplotlib/titanic.csv")
titanic = titanic.dropna(subset=["Age"])
plt.hist(titanic["Age"], bins=20, color="#00c40a", edgecolor="#000000")
plt.grid(axis="y",linestyle="dashed", alpha=0.5)
plt.show()