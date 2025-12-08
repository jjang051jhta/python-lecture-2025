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
    count = 0

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


class MoreFourCalc(FourCalc):
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    # pass #별다른 기능이 없을때 들여쓰기에 아무것도 없으면 오류이므로 오류 방지
    def pow(self):
        result = self.first**2
        return result

    # 메서드 오버라이드
    def divide(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


bb = MoreFourCalc(4, 0)
cc = MoreFourCalc(4, 0)
print(bb.add())
print(bb.divide())
print(bb.pow())

print(FourCalc.count)  # 클래스 변수는 class이름.class변수명으로 호출

bb.count = 10  # 이건 bb의 instance변수를 같은 이름으로 만들 수 있다
print("bb.count", bb.count)
print("bb.count", cc.count)  # cc.count는 0
FourCalc.count = 20  # 클래스 변수 값을 바꾸면 설정이 없는 인스턴스의 값은 바뀐다.
print("bb.count", bb.count)
print("bb.count", cc.count)
print(FourCalc.count)


# 파이썬은 다중 상속을 지원
class SuperCalc(FourCalc, MoreFourCalc):
    def __init__(self, first=0, second=0):
        FourCalc.__init__(self, first, second)
        MoreFourCalc.__init__(self, first, second)


calc = SuperCalc(10, 5)
