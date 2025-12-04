money = 3000
card = True
if card or money >= 4800:
    print("택시탈 수 있음")
else:
    print("걸어가야 함")

wallet = ["phone", "card", "money"]
if "money" in wallet:
    print("택시탈 수 있음")
else:
    print("걸어가야 함")
x = 5
print(x > 1 and x < 10)
print(1 < x < 10)
# 삼항연산자
age = 19
isAdult = False
if age >= 19:
    isAdult = True
else:
    isAdult = False
isAdult = False if age < 19 else True

if " ":
    print("빈문자열은 False 이므로 실행안됨")
else:
    print("빈문자열은 False이므로 else를 탐")
values = [0, 1, "", "python", [], [1], {}, {"a": 1}, True, False, None, (), (1)]
for value in values:
    print(value, "==>", bool(value))
if True:
    pass
else:
    print("여기는 출력 안됨")
score = 82
if score >= 90:
    print("a")
elif score >= 80:
    print("b")
elif score >= 70:
    print("c")
elif score >= 60:
    print("d")
else:
    print("f")

num = 1
while num <= 10:
    print(num)
    num += 1
num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break
num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
count = 0
while count < 5:
    count += 1
    print(count)
else:
    print("while문이 종료되었습니다.")

i = 1
while i <= 9:
    dan = 2
    while dan <= 9:
        print(f"{dan}x{i}={dan*i}", end="\t")
        dan += 1
    print()
    i += 1
fruits = ["apple", "berry", "madarin", "melon"]
for fruit in fruits:
    print(fruit)
list = [(1, 2), (3, 4), (5, 6)]
for first, second in list:
    print(first, ",", second)
for i in range(11):  # range(start, end)
    print(i)
fruits = ["apple", "berry", "madarin", "melon"]
for i in range(len(fruits)):
    print(fruits[i])

for dan in range(2, 10):
    for i in range(1, 10):
        print(f"{dan}x{i}={dan*i}")
    print()

for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan}x{i}={dan*i}", end="\t")
    print()
    
