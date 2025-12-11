import random

# print(random.random())  # 0~1사이 실수
# print(random.randint(1, 10))  # 1~10사이 정수


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


data = [1, 2, 3, 4, 5]
while data:
    print(random_pop(data), end=",")


def random_pop02(data):
    number = random.choice(data)
    data.remove(number)
    return number


print()
data = [1, 2, 3, 4, 5]
while data:
    print(random_pop02(data), end=",")

print()
data = [1, 2, 3, 4, 5]
print(random.choice(data))
print()
print(random.sample(data, 5))
print(random.shuffle(data))
print(data)

print("=" * 100)


def lotto():
    nums = random.sample(range(1, 46), 6)
    return sorted(nums)


for i in range(5):
    print(lotto())

winning_lotto = lotto()
print(f"당첨번호 : {winning_lotto}")
count = 0
while True:
    count += 1
    my_check_lotto = lotto()
    if my_check_lotto == winning_lotto:
        break
print(f"{count}만에 맞았습니다.")
