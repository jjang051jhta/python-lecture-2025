print(f"abs(-1) : {abs(-1)}")  # 절대값
print(f"abs(10) : {abs(10)}")  # 절대값

print(f"all([True, True, True]) : {all([True, True, True])}")
# all([iterable])  모든 요소가 참이면 True, 하나라도 거짓이면 False

print(f"all([True, True, False]) : {all([True, True, False])}")
print(f"all([0, 1, 2, 3]) : {all([0, 1, 2, 3])}")  # 0 은 Falsy 이므로 False
print(f"all([]) : {all([])}")  # 비어 있는 리스트는 True 반환
print(f"all([-1, -2]) : {all([-1, -2])}")  # 숫자는 0빼고 전부 True
print(f"all(['문자', '문자']) : {all(['문자', '문자'])}")  # 문자열은 True
print(f"all(['', '문자']) : {all(['', '문자'])}")  # 빈문자열은 False
print(
    f"all(num > 0 for num in [1, 2, 3, 4, 5]) : {all(num > 0 for num in [1,2,3,4,5])}"
)

# any()는 all()과 반대 → 하나라도 참이면 True
print(f"any([0, 1, 2, 3]) : {any([0, 1, 2, 3])}")
print(f"any([0, '']) : {any([0, ''])}")

print(f"chr(97) : {chr(97)}")  # chr() → 유니코드 숫자를 문자로 변환
print(f"chr(65) : {chr(65)}")
print(f"chr(44032) : {chr(44032)}")
print(f"chr(44033) : {chr(44033)}")
print(f"chr(44034) : {chr(44034)}")

print(f'ord("a") : {ord("a")}')

print(f"dir([1, 2, 3]) : {dir([1, 2, 3])}")
print(f"dir({{'name': '장성호'}}) : {dir({'name': '장성호'})}")
print(f"dir('string') : {dir('string')}")

print(f"7 // 3 : {7 // 3}")
print(f"7 % 3 : {7 % 3}")
print(f"divmod(7, 3) : {divmod(7, 3)}")  # 몫과 나머지를 tuple로 반환

print(f"eval('1+2') : {eval('1+2')}")
print(f"eval('divmod(7, 3)') : {eval('divmod(7, 3)')}")

print(f"hex(256) : {hex(256)}")

a = 3
print(f"id(a) : {id(a)}")
print(f"id(3) : {id(3)}")

b = a
print(f"id(b) : {id(b)}")
print(f"id(4) : {id(4)}")
