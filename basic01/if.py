money = 3000
card = True
if card or money >= 4800:  # >,<,>=,<=,==,!=  비교연산자
    print("택시 탈 수 있음")
else:
    print("걸어가야함")

isIn = 1 not in [1, 2, 3]
print(isIn)

wallet = ["phone", "card", "money"]
if "phone" in wallet:
    print("택시가능")
else:
    print("걸어가라")
x = 5
print((x > 1) and (x < 10))
print(1 < x < 10)
if x > 10:
    print("x는 10보다 큽니다.")
elif x > 5:
    print("x는 5보다 큽니다.")
else:
    print("x는 이하입니다.")

# input 두개 받아서 로그인 처리
"""
userID = "jjang051"
userPW = "1234"
inputID = input("아이디를 입력 : ")
inputPW = input("패스워드를 입력 : ")
if userID == inputID and userPW == inputPW:
    print("로그인 성공")
else:
    print("로그인 실패")
"""
age = 19
if age >= 19:
    pass
else:
    print("미성년자 입장불가")

score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result)
# python 3항 연산자
result = "합격" if score >= 60 else "불합격"
# 변수 = 참일때 값 if 조건 else 거짓일때 값
print(result)
# 19이상이면 성인 아니면 미성년자 출력
age = 19
isAdult = "성인" if age >= 19 else "미성년"
print(isAdult)
