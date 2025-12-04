def add(a, b):
    return a + b


print(add(10, 10))
# lambda는 한줄짜리 함수 def를 쓰지 않는다
# 익명함수 즉 이름없는 함수이다.
add = lambda a, b: a + b
print(add(3, 5))
square = lambda x: x**2
print(square(3))
say = lambda: "hello"
print(say())
is_even = lambda x: "짝수" if x % 2 == 0 else "홀수"
print(is_even(3))

# filter, map, sorted
nums = [1, 2, 3, 4, 5]


def double(x):
    return x * 2


# result = list(map(double, nums))
result = list(map(lambda x: x * 2, nums))
print(result)


def is_even02(x):
    return x % 2 == 0


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
result02 = list(filter(is_even02, nums))
print(result02)

result02 = list(filter(lambda x: x % 2 == 0, nums))
print(result02)

students = [("홍길동", 90), ("강감찬", 70), ("이순신", 85)]


def get_score(student):
    return student[1]


# result = sorted(students, key=get_score, reverse=True)
result = sorted(students, key=lambda student: student[0])
print(result)

students_dic = [
    {"name": "홍길동", "age": 20},
    {"name": "강감찬", "age": 15},
    {"name": "이순신", "age": 30},
]


def get_max_age(students):
    return students["age"]


oldest = max(students_dic, key=get_max_age)
print(oldest.get("name"), "==", oldest.get("age"))
# filter,max,min,map,sorted 등의 매개변수에 한줄짜리 lambda를 많이 쓴다.
