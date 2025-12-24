import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv("./matplotlib/titanic.csv")
print(titanic.info(),"\n")
print("="*100)
titanic = titanic.dropna(subset=["Age","Fare","Survived"])
print(titanic.info(),"\n")
# scatter 흩뿌리다 산점도 그래프
plt.figure(figsize=(12,8))  #단위는 inch이다
two_colors = ListedColormap(["#004edf","#7E7E7E"])
#scatter = plt.scatter(x="Age",y="Fare", data=titanic, c=titanic["Survived"], cmap="Set1", alpha=0.75)
scatter = plt.scatter(x="Age",y="Fare", data=titanic, c=titanic["Survived"], cmap=two_colors, alpha=0.75)
#c는 색상기준(생존여부), cmap=컬러팔레트 (Set1, Set2,Set3)
plt.colorbar(scatter,label="Survived (0=dead,1=survive)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()