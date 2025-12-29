# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


tips = sns.load_dataset("tips")  #seaborn에서 제공하는 tips 데이터셋 로드
print(tips.head())
figure = plt.figure(figsize=(15,5))
ax01 = figure.add_subplot(1,2,1)  #가로 한줄에 2개의 그래프 배치 1번째 그래프
ax02 = figure.add_subplot(1,2,2)  #가로 한줄에 2개의 그래프 배치 2번째 그래프
sns.countplot(x="time", data=tips,ax=ax01)
sns.countplot(x="time", data=tips,palette="Set2", hue="day", ax=ax02)
ax01.set_title("시간별 팁의 빈도수")
ax02.set_title("시간별 팁의 빈도수 (요일별)")
plt.show()
