# heatmap (컬러로 변환된 2D 배열 시각화)
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"   # 윈도우 기본 한글 폰트
plt.rcParams["axes.unicode_minus"] = False  
titanic = pd.read_csv("./matplotlib/titanic.csv")
titanic = titanic.dropna(subset=["Age","Fare"])

correlation_matrix= titanic.drop("PassengerId", axis=1).corr(numeric_only=True)
print(correlation_matrix)  #-1.0 ~ 1.0을 갖는 상관계수 행렬
# Fared와 Survived가 양의 상관관계는 양의 상관 관계 요금이 높을수록 생존확율이 높아짐  0.2~0.3 정도가 유의미함
# fig, ax = plt.subplots(figsize=(8, 7))  #구조분해  그래프 여러개 그릴때 사용
# cax = ax.matshow(correlation_matrix, cmap="PuRd_r")
# fig.colorbar(cax)
#plt.subplots(figsize=(8, 7))  #구조분해  그래프 여러개 그릴때 사용
plt.matshow(correlation_matrix, cmap="PuRd_r")
plt.colorbar()

# ax.set_xticks(range(len(correlation_matrix.columns)))
# ax.set_yticks(range(len(correlation_matrix.columns)))
# ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha="left")
# ax.set_yticklabels(correlation_matrix.columns)
plt.xticks(range(len(correlation_matrix.columns)),correlation_matrix.columns, rotation=45, ha="left")
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        value  = correlation_matrix.iloc[i, j]
        plt.text(j, i, f"{value:.2f}",
                ha="center", va="center", color="black", fontsize=9)

plt.tight_layout()
plt.title("상관계수 히트맵")

plt.show()