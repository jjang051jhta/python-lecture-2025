def add(a, b):
    return a + b


print(add(10, 10))


def say():
    return "hello"


print(say())


def add02(a, b):
    print(f"{a}+{b}={a+b}")


add02(10, 10)

print(add(a=10, b=20))
print(add(10, 20))
print(add(b=10, a=20))


def add_many(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add_many(10, 10, 10, 10, 10))


def show_profile(name, **kargs):
    print(f"name:{name}")
    for key, value in kargs.items():
        print(f"{key}:{value}")


show_profile("장성호", age=20, address="일산", hobby="넷플릭스")

# order 메뉴는 인수로 받고 , 수량은 DEFAULT=1,takeout=False, 나머지는 option


def order(menu, qty=1, *, takeout=False, **option):
    print(f"menu:{menu}")
    print(f"수량:{qty}")
    print(f"takeout:{takeout}")
    # print(f"옵션:{option}")
    for key, value in option.items():
        print(f"{key}:{value}")


order("아메리카노", 2, takeout=True, size="tall", shot=2)

add = lambda a, b: a + b  # lambda는 한줄 함수표현식(function expression)
print(add(10, 20))
square = lambda x: x**2
print(square(10))
# map/filter/sorted
nums = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(map(lambda num: num**2, nums)))
print(list(filter(lambda num: num % 2 == 0, nums)))
print(list(sorted(nums, key=lambda num: num)))
students = [
    {"name": "김유신", "age": 20},
    {"name": "이순신", "age": 30},
    {"name": "강감찬", "age": 25},
]
print(list(sorted(students, key=lambda student: student["age"])))
print(list(sorted(students, key=lambda student: student["name"])))
