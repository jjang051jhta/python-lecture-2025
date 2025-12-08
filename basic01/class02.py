class FourCalc:
    # self는 자기 자신을 가리키는 키워드  자바에 this와 같다.
    # 파이썬은 생성자 오버로딩이 없다. 필요하면 기본값을 세킹해두는 방식을 이용한다.
    count = 0

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

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


class MoreFourCalc:
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


# 다중 상속을 통한 SuperCalc 클래스
class SuperCalc(FourCalc, MoreFourCalc):  # 함수의 매개변수처럼 사용
    def __init__(self, first=0, second=0):
        # 두 부모 클래스의 생성자를 각각 호출
        FourCalc.__init__(self, first, second)
        MoreFourCalc.__init__(self, first, second)
