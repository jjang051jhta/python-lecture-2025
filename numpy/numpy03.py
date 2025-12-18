import numpy as np
nums = np.array([10, 3, 5, 7, 2,2,2,2,3,9,12,15,18])
unique_nums = np.unique(nums)
print(unique_nums)
prices = np.array([10000,20000,30000,40000,50000])
vat = prices * 0.1
total_prices = prices + vat
print(f"부가세 : {vat}")
print(f"총 가격 : {total_prices}")  
#파이썬의 리스트는 편하긴 한데 속도는 느리다.

a01 = np.arange(1, 13)
b02 = a01.reshape(4,3)
print(b02)

for i in range(1,6):
  lotto = np.random.choice(range(1, 46), size=6, replace=False)
  print(f"{i} : {np.sort(lotto)}")

a02 = np.array([[1,2,3],[4,5,6]])
a03 = np.array([[7,8,9]])
result = np.concatenate((a02,a03), axis=0 )
print(result)  # 행 기준으로 합치기
result02 =  a02+a03
print(result02)

ones = np.ones((3,5))
print(ones)
zeros = np.zeros((3,5))
print(zeros)

print(np.random.random((3,2)))