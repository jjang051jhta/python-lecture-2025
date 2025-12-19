# numpy  / pandas
import numpy as np
np_array01 = np.array([1, 2, 3])
np_array02 = np.array([4,5,6])
print(np_array01)
print(np_array01*2)
print(np_array01+np_array02)
print(type(np_array01))
print(np_array01.dtype)
np_array03 = np.array([ [1,2,3]
                       ,[4,5,6]
                       ,[7,8,9]]
                       )
print(np_array03)
np_array04 = np.array([[
                        [1,2,3]
                       ,[4,5,6]
                       ]
                       ,[
                         [7,8,9],
                         [10,11,12]
                        ]
                       ,[
                         [12,14,15],
                         [16,17,18]
                        ]
                       ])
print(np_array04)
print(np_array04[0][0][2])
print(f"np_array01.shape = {np_array01.shape}")
print(f"np_array03.shape = {np_array03.shape}") #shape은 축을 기준으로 크기를 튜플로 반환
print(f"np_array03.ndim = {np_array03.ndim}") #ndim은 차원의 수를 반환
print(f"np_array04.ndim = {np_array04.ndim}") #ndim은 차원의 수를 반환
print(f"np_array01.size = {np_array01.size}") #size 요소의 갯수를 반환
print(f"np_array03.size = {np_array03.size}") 
print(f"np_array04.size = {np_array04.size}") 


np_array05 = np.arange(12).reshape(4,3)
print(np_array05)

# 3차원 배열 0~100사이의 점수를 각 반에 4명의 학생이 있고 3개의 과목을 가지고 있는 
# 배열  점수는 랜덤으로
scores = np.random.randint(0,101,size=(3,4,3))
print(scores)
for class_idx in range(scores.shape[0]):
  print(f"{class_idx+1}반 성적")
  for student_idx in range(scores.shape[1]):
      korean,eng,math = scores[class_idx,student_idx]
      print(f"  {student_idx+1}번 학생: 국어={korean}, 영어={eng}, 수학={math}")

zeros = np.zeros((3,4))
print(zeros)
ones = np.ones((3,4))
print(ones)
empties = np.empty((3,4))
print(empties)
np_arange = np.arange(start=10, stop=32, step=2, dtype=int)
print(np_arange)
np_arange = np.arange(start=0, stop=2.1, step=0.1, dtype=float)
print(np_arange)
np_linespace = np.linspace(start=1, stop=100, num=100,endpoint=True, dtype=int)
print(np_linespace)

np_linespace02 = np.linspace(start=1, stop=10, num=5,endpoint=True)
print(f"np_linespace02={np_linespace02}")
np_linespace03 = np.linspace(start=1, stop=10, num=5,endpoint=False)
print(f"np_linespace03={np_linespace03}") 
#(stop-start) / (num-1) = 2.4  endpoint=True
#(stop-start) / num = 1.8  endpoint=False

np_linespace04 = np.linspace(start=1, stop=10, num=5,retstep=True,endpoint=True) 
#retstep= default가 False,endpoint=default가 True
print(f"np_linespace04={np_linespace04}")
arr, step = np_linespace04
print(f"arr={arr}, step={step}")

a = np.array([10,20,30,40])
b = np.arange(start=1, stop=5)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
aa =  np.array([[1,1],[0,1]])
bb =  np.array([[2,0],[3,4]])
print(aa*bb)
print(aa @ bb)  #@는 행렬곱 