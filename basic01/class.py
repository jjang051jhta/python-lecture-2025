"""
result01 = 0
result02 = 0


def add01(num):
    global result01
    result01 += num
    return result01


def add02(num):
    global result02
    result02 += num
    return result02


print(add01(10))
print(add02(10))
print(add01(10))
print(add02(10))
"""


class Calculator:
    def __init__(self):
        self.result = 0  # 생성자 함수 초기값 설정할때 쓴다.

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


calculator01 = Calculator()
print(calculator01.add(10))
print(calculator01.sub(5))


class FourCalc:
    # self는 자기 자신을 가리키는 키워드  자바에 this와 같다.
    # 파이썬은 생성자 오버로딩이 없다. 필요하면 기본값을 세킹해두는 방식을 이용한다.

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    """
    def __init__(self, *args):
        if len(args) == 0:
            self.first = 0
            self.second = 0
        elif len(args) == 1:
            self.first = args[0]
            self.second = 0
        elif len(args) == 2:
            self.first = args[0]
            self.second = args[1]
        else:
            raise ValueError("매개변수는 2개 이상일 수 없습니다.")
    """

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def multiple(self):
        result = self.first * self.second
        return result

    def divide(self):
        result = self.first / self.second
        return result


aa = FourCalc()
print(type(aa))
# aa.setdata(10, 20)
print(aa.add())
print(aa.sub())
print(aa.multiple())
# print(aa.divide())
