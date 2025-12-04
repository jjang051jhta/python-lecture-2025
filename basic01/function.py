def add(a, b):
    return a + b


result = add(10, 5)
print(result)


def say():
    return "hello"


print(say())


def add02(a, b):
    print(f"{a},{b}의 합은 {a+b}")


add02(10, 5)


def say02():
    print("say hello")


say02()


result = add(a=10, b=10)
print(result)


def minus(a, b):
    return b - a


result = minus(b=10, a=3)
print(result)


def add_many(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add_many(10, 10))


def add_many01(choice, *args):
    if choice == "add":
        result = 0
        for num in args:
            result += num
        return result
    elif choice == "multiple":
        result = 1
        for num in args:
            result *= num
    return result


print("add===", add_many01("add", 1, 2, 3, 4, 5))
print("mul===", add_many01("multiple", 1, 2, 3, 4, 5))


def print_keyword(**kargs):
    print(kargs)


print_keyword(a=1, b=2)
print_keyword(name="장성호", age=20)


def mix_func(name, *args, **kargs):
    print(f"name:{name}")
    print(f"list:{args}")
    print(f"dic:{kargs}")


mix_func("장성호", 1, 2, 3, 4, 5, age=20, address="일산")


def add_and_mutiple(a, b):
    return a + b, a * b  # 컴마로 구분하면 tuple로 리턴한다.


print(add_and_mutiple(10, 2))
result01, result02 = add_and_mutiple(10, 2)
print(result01, "==", result02)


def show_profile(name, age, man=True):
    print(f"name:{name}")
    print(f"age:{age}")
    if man:
        print("남자")
    else:
        print("여자")


show_profile("장성호", True)
show_profile("전지현", False, 20)

a = 1


def var_test():
    # a는 지역변수로 동작
    global a  # global을 붙이면 전역 변수가 된다. 사용을 하지 않는게 좋다.
    a += 1


var_test()
print(a)


def add03(a, b):
    """
    두개의 매개변수를 더하는 함수
    :param a(number)
    :param b(number)
    """
    return a + b


print(add03(10, 10))
print(add03.__doc__)


# 1. 숫자를 절대값으로 반환하는 함수 abs 사용 금지
# 2. 리스트에서 짝수만 반환하는 함수


def func_abs(num):
    return num if num >= 0 else -num


print(func_abs(10))
print(func_abs(-10))


def get_even(nums):
    """


    :param nums: list
    :return even_list
    """
    return [num for num in nums if num % 2 == 0]


print(get_even([2, 3, 4, 5, 6, 7, 8, 9]))
print(get_even.__doc__)
