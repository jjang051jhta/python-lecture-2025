import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv("./matplotlib/titanic.csv")
survived_count = titanic["Survived"].value_counts()
#print(survived_count)
plt.figure(figsize=(8,8))
wedges, texts,autotexts = plt.pie(survived_count,
        labels=["Dead", "Survived"], 
        colors=["#df9100","#ffcb6b"],
        startangle=90,
        shadow=True,
        #wedgeprops={"alpha":0.85},
        explode=(0,0.1),
        autopct="%0.1f%%"
        )
#print(wedges)
for t in autotexts:
  t.set_fontsize(20)
plt.show()