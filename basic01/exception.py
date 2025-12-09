# result = 4 / 0
# print(result)

# nums = [1, 2, 3]
# print(nums[3])

# f = open("알 수 없는 파일", "r")
"""
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

f = None
try:
    f = open("알 수 없는 파일", "r")
except FileNotFoundError as e:
    print(e)
finally:
    print("파일을 닫습니다.")
    if f is not None:
        f.close()

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱안됩니다.")


try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

"""
try:
    age = int(input("나이를 입력하세요 : "))
except:
    print("입력이 올바르지 않습니다.")
else:
    if age <= 18:
        print("미성년자 출입금지")
    else:
        print("환영합니다.")
