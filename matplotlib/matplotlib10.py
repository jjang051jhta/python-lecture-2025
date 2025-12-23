import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"   # 윈도우 기본 한글 폰트
plt.rcParams["axes.unicode_minus"] = False  
titanic = pd.read_csv("./matplotlib/titanic.csv")
survived_count = titanic[titanic["Survived"]==1]["Sex"].value_counts()
#print(survived_count)
survived_count = titanic[titanic["Survived"]==1]["Sex"].value_counts()
bars = plt.barh(survived_count.index,survived_count,color=["#ff0000","#0095f8"])
plt.title("생존자 남녀비율")
plt.xlabel("Count", labelpad=10, fontweight="bold")
plt.ylabel("성별", labelpad=3, fontweight="bold")
plt.axvline(x=survived_count["male"],color="#cccccc", linestyle="dashed", linewidth=1)
for i, value in enumerate(survived_count):
  plt.text(value+1,i, str(value),ha="left", va="center")
plt.show()