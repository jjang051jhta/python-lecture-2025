# 파이썬 클래스는 접근제어자가 따로 없다.
# 함수로 정의된다.
# 자기자신을 가리키는 java this는 self로 쓴다.
# 생성자 오버로딩이 없다. 즉 여러개의 생성자를 만들 수 없다
class Calculator:
    def __init__(self, first=0, second=0):
        self.result = 0
        self.first = first
        self.second = second

    def add(self, num=1):
        self.result += num
        return self.result


calculator = Calculator(1, 1)
print(calculator.add())
print(calculator.first)


# 파이썬 클래스는 상속을 할때 extend 와 같은 키워드가 없다. 괄호안에 매개변수로 부모타입을 넣으면 된다.
# super()가 부모호출한다.
# self는 인스턴스가 만들어진 후에 생기는 값이다.
class AdvancedCalculator(Calculator):
    def __init__(self, first=0, second=0):
        super().__init__(first, second)

    def pow(self, num=None):
        if num == None:
            num = self.first
        result = num**2
        return result


# 만약 pow의 매개변수가 없으면 first를 가지고 만약 있으면 그 값을 제곱하게 하고 싶을때
ac = AdvancedCalculator(3, 5)
print(ac.pow(10))

# 파이썬 클래스는 다중 상속이 가능


class AnotherCalsulator:
    def __init__(self, first=0, second=0):
        self.result = 0
        self.first = first
        self.second = second

    def multiple(self):
        result = self.first * self.second
        return result


class SuperCalculator(Calculator, AnotherCalsulator):
    pass


sc = SuperCalculator(10, 2)
print(sc.multiple())
print(sc.add())


# 접근제어자가 없다 즉 getter/setter가 없다.
class Person:
    def __init__(self, name):
        self._name = name

    # getter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


p = Person("홍길동")
p.name = "아무개"
print(p.name)
