class FourCalc:
    count = 0

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def multiple(self):
        return self.first * self.second

    def divide(self):
        if self.second == 0:
            return "0으로 나눌 수 없습니다!"
        return self.first / self.second


class MoreFourCalc:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def pow(self):
        return self.first**2

    def divide(self):
        if self.second == 0:
            return "0으로 나눌 수 없습니다!"
        return self.first / self.second


# 다중 상속을 통한 SuperCalc 클래스
class SuperCalc(FourCalc, MoreFourCalc):
    def __init__(self, first=0, second=0):
        # 두 부모 클래스의 생성자를 각각 호출
        FourCalc.__init__(self, first, second)
        MoreFourCalc.__init__(self, first, second)
