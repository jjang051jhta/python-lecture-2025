print(True)
print(False)
print(type(False))
print(1 == 1)
print(2 > 1)
print(2 < 1)
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
# truthy  /  falsy

print(bool("python"))
print(bool(""))  # 빈 문자열은 falsy
print(bool(" "))  # 공백 문자열은 truthy
print(bool([1, 2, 3]))  # 리스트에 값이 있으면 truthy
print(bool([]))  # 빈 리스트는 falsy
print(bool((1, 2, 3)))  # 튜플에 값이 있으면 truthy
print(bool(()))  # 빈 튜플은 falsy
print(bool({"name": "장성호"}))  # 딕셔너리에 값이 있으면 truthy
print(bool({}))  # 빈 딕셔너리는 falsy
print(bool(None))  # None은 falsy
