import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"   # 윈도우 기본 한글 폰트
plt.rcParams["axes.unicode_minus"] = False  
titanic = pd.read_csv("./matplotlib/titanic.csv")
#print(titanic)
survived_count = titanic[titanic["Survived"]==1]["Embarked"].value_counts()
#print(survived_count)
#print(titanic[titanic["Survived"]==1]["Embarked"].value_counts())
plt.bar(survived_count.index, survived_count,
        color=["#ff0000","#1de627","#007adf"])
plt.title("승선 항구별 생존자 수")
plt.xlabel("승선항구", labelpad=10, fontweight="bold")
plt.ylabel("생존자수", labelpad=10, fontweight="bold")
plt.ylim(0,survived_count.max()+30)
plt.xticks(survived_count.index,["Southampton","Cherbourg","Queenstown"])
plt.grid(axis="y",linestyle="dashed", alpha=0.5)
for i, value in enumerate(survived_count):
  plt.text(i,value+1, str(value),ha="center", va="bottom")
plt.show()