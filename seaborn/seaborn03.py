# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

tips = sns.load_dataset("tips")
fig=plt.figure(figsize=(15, 6))
ax01 = fig.add_subplot(1,2,1)
ax02 = fig.add_subplot(1,2,2)
sns.regplot(x="total_bill", y="tip", data=tips, color="blue",ax=ax01,
            scatter_kws={"s":50, "alpha":0.5},  #산점도 옵션
            line_kws={"color":"red", "lw":2, "linestyle":"--"},  #회귀선
            fit_reg=True
            )
ax01.set_title("선형회귀선이 포함된 그래프")

sns.regplot(x="total_bill", y="tip", data=tips, color="blue",ax=ax02,
            scatter_kws={"s":50, "alpha":0.5},  #산점도 옵션
            line_kws={"color":"red", "lw":2, "linestyle":"--"},  #회귀선
            fit_reg=False
            )
ax02.set_title("선형회귀선이 포함되지 않은 그래프")
fig.suptitle("total_bill과 tip의 관계", fontsize=16 )
plt.show()