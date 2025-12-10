print(abs(-1))  # 절대값
print(abs(10))  # 절대값
print(
    all([True, True, True])
)  # all([iterable,문자, 튜플 등등])  모든 요소가 참이면 참 하나라도 거짓이면 거짓
print(all([True, True, False]))
print(all([0, 1, 2, 3]))  # 0 은 Falsy 이므로 false
print(all([]))  # 비어 있는 리스트는 True 반환
print(all([-1, -2]))  # 숫자는 0빼고는 전부 True
print(all(["문자", "문자"]))  # 문자열은 True
print(all(["", "문자"]))  # 빈문자열은 False
print(all(num > 0 for num in [1, 2, 3, 4, 5]))
# any()는 all()과 반대 하나라도 참이면 참
print(any([0, 1, 2, 3]))
print(any([0, ""]))
print(chr(97))  # chr()은 유니코드 값을 받아서 문자 출력
print(chr(65))
print(chr(44032))
print(chr(44033))
print(chr(44034))
print('ord("a")', ord("a"))
print(dir([1, 2, 3]))
print(dir({"name": "장성호"}))
print(dir("string"))
print(7 // 3)
print(7 % 3)
print(divmod(7, 3))  # 몫과 나머지를 한번에 돌려준다. tuple로 돌려준다.
print(eval("1+2"))  # input()으로 넘어온 문자열 그냥 계산할때 쓴다.
print(eval("divmod(7, 3)"))  # input()으로 넘어온 문자열 그냥 계산할때 쓴다.
print(hex(256))
a = 3
print(id(a))
print(id(3))
b = a
print(id(b))
print(id(4))
