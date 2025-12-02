#변수명 = 값
num01=10
num02=3.14
num03=0o17
num04=0x2a
print(num01,num02,num03,num04)
print(num01+num01)
print(num01*num01)
print(num01**3) #제곱
print(num01/num01)
print(num01-num01)
print(num01//3) #몫
print(num01%3)  #나머지

str01 =  """hello python"""  #리스트로 관리
print(str01+"!!!")
print(str01*3)  #문자열에 곱하기 연산 가능
print(str01[0]+str01[1]+str01[2]+str01[3]+str01[4])
print(str01[0:5])
print(str01[0:])
print(str01[2:5])
print(str01[0:10:2])  # [start:end:step]  
print(str01[::-2])  # [start:end:step]
print("I {0} {1}".format("hate","python"))
print("I {emotion} {language}"
      .format(language="python",emotion="hate"))
emotion= "love"
print(f"I {emotion} python")
a=3
b=5
print(f"{a}+{b}={a+b}")
print(f"{'hi':<10}!!")
print(f"!!{'hi':>10}")
print(f"!!{'hi':^10}!!")
print(f"{'hi':=<10}!!")
print(f"{'hi':=>10}!!")
print(f"!!{'hi':=^10}!!")
print(f"{1500000:,}")  # , 넣으면 3자리마다 , 넣어준다.
