# 배열연산할때 주로 사용
# pip install numpy
import numpy as np
a = [1,2,3]
b = [4,5,6]
print(a+b)
# 리스트는 + 연산자가 단순히 이어붙이기만 함
a01 =  np.array([1,2,3])
b01 =  np.array([4,5,6])
print(a01+b01) 
a02 =  np.array(a)
b02 =  np.array(b)
print(a02+b02) 
print(type(a))
print(a01.dtype)
a03 = np.array([1,2,3,"문자열"])
# a01[0] = "문자열" 오류남 # numpy 배열은 같은 자료형만 저장 가능
print(a03)  #같은 타입으로 들어가야 하기 때문에 숫자를 문자로 바꿈
print(a03.dtype)  # <U21  유니코드
a04 = np.array([1,2,3,3.14])
print(a04)
print(a04.dtype)  # float64  일반적인 자바 배열 형태  C언어 형태 연산이 빠름
