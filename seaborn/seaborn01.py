# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")  #seaborn에서 제공하는 tips 데이터셋 로드
print(tips.head())
#figure = plt.figure(figsize=(15,5))
#ax01 = figure.add_subplot(1,2,1)  #가로 한줄에 2개의 그래프 배치 1번째 그래프
#ax02 = figure.add_subplot(1,2,2)  #가로 한줄에 2개의 그래프 배치 2번째 그래프
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))  #가로 한줄에 2개의 그래프 배치
ax01 = axes[0]
ax02 = axes[1]

#stripplot: 데이터 포인트를 범주형 축을 따라 수직선 상에 무작위로 분산시켜 표시
sns.stripplot(x="day", y="tip", hue="sex",data=tips, alpha=0.7, ax=ax01) 
#swarmplot: 데이터 포인트가 겹치지 않도록 조정하여 표시
sns.swarmplot(x="day", y="tip", hue="sex",data=tips, alpha=0.7, ax=ax02, 
              palette="Set2")
ax01.set_title("stripplot of tips by day and sex")
ax02.set_title("swarmplot of tips by day and sex")
plt.show()
