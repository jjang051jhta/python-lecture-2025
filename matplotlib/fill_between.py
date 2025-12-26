import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv("./matplotlib/titanic.csv")
titanic = titanic.dropna(subset=["Age","Fare"])
age_groups = pd.cut(titanic["Age"], bins=range(0,81,5))
#print(age_groups)
survived_counts = titanic.groupby([age_groups,"Survived"], observed=False).size().unstack().fillna(0)
print(survived_counts)
#observed=False  관측되지 않은 범주도 결과에 포함해라 True 면 관측되지 않으면 결과에서 배제
# size() 는 행의 갯수 세기
#면적 그래프
plt.fill_between(survived_counts.index.astype(str), survived_counts[1], color="#8507fc",alpha=0.9, label="Survived")
plt.fill_between(survived_counts.index.astype(str), survived_counts[0], color="#ff8d8d",alpha=0.5, label="Dead")
plt.xlabel("Age")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()