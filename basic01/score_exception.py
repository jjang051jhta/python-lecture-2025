students = ["홍길동", "이순신", "김유신", "강감찬"]
for student in students:
    try:
        with open(f"basic01/score/{student}.txt", "r", encoding="utf-8") as f:
            score = f.read().strip()
            print(f"{student}의 성적 : {score}")
    except FileNotFoundError as e:
        # print(f"{student}의 파일이 없습니다.")
        continue

"""
두 숫자를 입력받는다. (input 사용)

두 번째 숫자가 0일 경우 ZeroDivisionError를 처리하여
"0으로 나눌 수 없습니다." 라고 출력한다.

입력이 숫자가 아닐 경우 ValueError를 처리하여
"숫자만 입력하세요." 라고 출력한다.

정상적으로 계산된 경우 결과를 출력한다.
"""

try:
    a = int(input("첫번째 숫자 : "))
    b = int(input("첫번째 숫자 : "))
    result = a / b
    print(f"결과 : {result}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 입력하세요.")


class NegativeNumberError(Exception):
    """음수가 들어오면 발생되는 예외"""

    pass


def check_num(num):
    if num < 0:
        raise NegativeNumberError("음수는 사용할 수 없습니다.")
    print(f"정상입력 : {num}")


try:
    check_num(-5)
except NegativeNumberError as e:
    print("예외 발생", e)


# 성적이 100 이상이면 발생하는 예외  ScoreError
class ScoreError(Exception):
    pass


def check_score(num):
    if num > 100:
        raise ScoreError("성적은 100 보다 클 수 없습니다.")
    print(f"정상입력 : {num}")


try:
    check_score(110)
except ScoreError as e:
    print("예외 발생", e)
