# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#histogram: 연속형 변수를 구간(bins)으로 나누어 각 구간에 속하는 데이터의 빈도수를 막대그래프로 표현
tips = sns.load_dataset("tips")
print(tips.head())
sns.pairplot(tips, vars=["total_bill", "tip","size"], hue="sex", palette="husl",diag_kind="hist")  #hue: 성별에 따라 색상 구분
#paitrplot: 데이터셋의 모든 수치형 변수들 간의 관계를 산점도와 히스토그램으로 시각화
plt.suptitle("Tips 데이터셋의 Pairplot", y=1.05) 
plt.show()