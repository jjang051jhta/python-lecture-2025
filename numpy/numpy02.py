import numpy as np
scores = np.array([
      [80,90,75],
      [100,63,77],
      [88,92,93],
])
total = scores.sum()
print(f"전체 합 : {total}")
row_total = scores.sum(axis=1)
print(f"행의 전체 합 : {row_total}")
col_total = scores.sum(axis=0)
print(f"열의 전체 합 : {col_total}")
mean = scores.mean()
print(f"전체 평균 : {mean}")  
row_mean = scores.mean(axis=1)
print(f"행의 평균 : {row_mean}")    
col_mean = scores.mean(axis=0)
print(f"열의 평균 : {col_mean}")
print(f"최대값 : {scores.max()}")
print(f"최소값 : {scores.min()}")

a01 = np.array([10,20,30,40,50])
print(a01.std())  # 표준편차  표준에서 벗어난 정도  평균이 있을때 흩어진 정도

passed = a01[a01 >= 30]
print(f"30점 이상 : {passed}")

avg = scores.mean(axis=1)
masking = avg>=85
print(f"85점 이상 여부 : {masking}")
print(f"85점 이상 학생 : {scores[masking]}")

result = np.where(a01>=70,"합격", "불합격")  # 30점 이상이면 점수 유지, 아니면 0으로 변경
print(result)