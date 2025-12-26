import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv("./matplotlib/titanic.csv")
titanic = titanic.dropna(subset=["Age","Fare"])
#axix가 0이면 행(row) 제거 1임녀 열(column)제거
#.corr()은  상관관계를 행렬 연산해준다.
#피어슨상관계수 (-1 ~ 0 ~  1) 값이 나옴
correlation_matrix = titanic.drop("PassengerId",axis=1).corr(numeric_only=True)  
print(correlation_matrix) 
# -1 ~ 1 1은 양의 상관관계 완벽한 일치, 
#       -1은 반대의 의미  
#        0에 가까우면 서로 관계 없다라고 생각하면 됨
my_cmap = ListedColormap(["#69e901","#f8f8f8","#ff0000"])
#plt.matshow(correlation_matrix, cmap=my_cmap) 이렇게 쓰면 색상이 3개만 나옴
plt.matshow(correlation_matrix, cmap="PuRd_r")
#PuRd_r, coolwarm, RdBu_r
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.colorbar()
plt.show()

