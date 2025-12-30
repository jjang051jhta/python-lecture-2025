# pip install seaborn
import seaborn as sns  #seaborn의 별칭은 sns 사람이름  
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

print(sns.get_dataset_names())  #seaborn에서 제공하는 데이터셋 목록 확인

tips = sns.load_dataset("tips")
print(tips.head())  #tips 데이터셋의 처음 5행 출력

fig = plt.figure(figsize=(15, 6))
ax01 = fig.add_subplot(1,2,1)
ax02 = fig.add_subplot(1,2,2)
"""
sns.countplot(data=tips, x="time", ax=ax01)
sns.countplot(data=tips, x="time", ax=ax02, palette="Set2", hue="day")
ax01.set_title("시간별 팁의 빈도 수")
ax02.set_title("시간별 팁의 빈도 수 (요일별)")
print("="*100)
for p in ax01.patches:
  height= p.get_height()

  ax01.text(
    p.get_x()+p.get_width()/2,
    height + 0.1,
    height,
    ha="center",
    va="bottom"
  )
for p in ax02.patches:
  height= p.get_height()
  if height==0:
    p.set_visible(False)
    continue
  ax02.text(
    p.get_x()+p.get_width()/2,
    height + 0.1,
    height,
    ha="center",
    va="bottom"
  )
ax01.grid(axis="y", linestyle="--", alpha=0.5)
ax02.grid(axis="y", linestyle="--", alpha=0.5)
ax01.set_axisbelow(True)
ax02.set_axisbelow(True)
plt.show()
"""

sns.countplot(data=tips, y="time", ax=ax01)
sns.countplot(data=tips, y="time", ax=ax02, palette="Set2", hue="day")
ax01.set_title("시간별 팁의 빈도 수")
ax02.set_title("시간별 팁의 빈도 수 (요일별)")
print("="*100)
print(ax01.get_xlim())  #x축 범위 확인
ax01.set_xlim(ax01.get_xlim()[0], ax01.get_xlim()[1]*1.05)  #x축 범위 조정
for p in ax01.patches:
  width= p.get_width()
  ax01.text(
    width + 0.1,
    p.get_y()+p.get_height()/2,
    width,
    va="center",
    ha="left"
  )
ax02.set_xlim(ax02.get_xlim()[0], ax02.get_xlim()[1]*1.05)  #x축 범위 조정  
for p in ax02.patches:
  width= p.get_width()
  if width==0:
    p.set_visible(False)
    continue
  ax02.text(
    width + 0.1,
    p.get_y()+p.get_height()/2,
    width,
    va="center",
    ha="left"
  )
ax01.grid(axis="y", linestyle="--", alpha=0.5)
ax02.grid(axis="y", linestyle="--", alpha=0.5)
ax01.set_axisbelow(True)
ax02.set_axisbelow(True)
plt.show()
#그래프를 가로로 바꿔 보세요