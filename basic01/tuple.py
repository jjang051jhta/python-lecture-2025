# 불변객체 수정 추가 삭제 등이 되지 않는다
tuple01 = (1, 2, 3)
tuple02 = (1,)
faketuple02 = 1
tuple03 = 1, 2, 3
print(tuple01)
print(type(tuple02))
print(type(faketuple02))
print(tuple01[0])
#del tuple01[0]
