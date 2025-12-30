# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#histogram: 연속형 변수를 구간(bins)으로 나누어 각 구간에 속하는 데이터의 빈도수를 막대그래프로 표현
tips = sns.load_dataset("tips")
sns.jointplot(x="size",y="tip", data=tips, kind="scatter", color="purple")
plt.show()