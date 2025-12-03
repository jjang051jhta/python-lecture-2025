hit = 0
while hit < 10:
    hit += 1
    print(f"나무를 {hit}번 찍었습니다.")
    if hit >= 10:
        print("10번찍은 나무가 넘어갑니다.")

prompt = """
  1. ADD
  2. MINUS
  3. MUTIPLE
  4. DIVIDE
  Enter number : 
"""
# print(prompt)
number = 0
"""
while number != 4:
    print(prompt)
    number = int(input())
"""
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
count = 0
while count < 10:
    print(f"count:{count}")
    count += 1
else:
    print("while문 종료")

"""
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
while True:
    num = int(input("3의 배수 입력 : "))
    if num % 3 != 0:
        print("3의 배수가 아닙니다. 다시 입력해 주세요.")
        continue
    print("정상입력 : ", num)
    break
"""
for i in range(5):  # range(숫자) 0~해당하는 숫자까지
    print(i)
print("===" * 10)
for i in range(1, 11, 2):  # range(숫자) 0~해당하는 숫자까지
    print(i)
print("===" * 10)
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
print("===" * 10)
for ch in "hello python":
    print(ch)
print("===" * 10)
scores = [90, 25, 76, 83, 92]

number = 0
for score in scores:
    number += 1
    if score > 80:
        print(f"{number}학생은 합격")
    else:
        print(f"{number}학생은 불합격")
print("===" * 10)
for i in range(10):
    print(i)
else:
    print("for문을 종료합니다.")

frutis = ["apple", "banana", "berry"]
for i, fruit in enumerate(frutis, 1):
    print(i, ":", fruit)
nums = []
for i in range(1, 101):
    nums.append(i)
print(nums)
# 리스트 컴프리헨션
nums = [i for i in range(1, 101)]
print(nums)
names = ["홍길동", "김유신", "이순신"]
scores = [90, 80, 95]
for i in range(3):
    print(names[i], ":", scores[i])
for name, score in zip(names, scores):
    print(name, ":", score)
students = [
    {"name": "홍길동", "score": 90},
    {"name": "김유신", "score": 80},
    {"name": "이순신", "score": 95},
]
for student in students:
    print(student["name"], ":", student["score"])
