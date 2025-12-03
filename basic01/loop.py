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
