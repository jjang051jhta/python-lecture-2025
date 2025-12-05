# 파일 python은 excel이랑 친하다.
f = open("basic01/new-file.txt", "w", encoding="utf-8")
f.write("hello python!!\n")
f.write("writing\n")
f.write("헬로 파이썬")
f.close()

f02 = open("basic01/poem.txt", "a", encoding="utf-8")
# content = f02.read()
# print(content)
f02.write("채영이가 좋아하는 랜덤게임")
f02.close()

f03 = open("basic01/poem.txt", "r", encoding="utf-8")
content = f03.read()
print(content)
f03.close()
"""
 w일때는 쓰기만 가능  r은 읽기만 가능  
 r+ 는 읽기 쓰기(덮어쓴다 기존 내용은 사라진다.)
 a 는 이어쓰기 가능 대신 읽기는 안됨
"""


# new-file02.txt만들고 1번째 줄입니다. ~~ 10 번째 줄입니다.

f04 = open("basic01/new-file02.txt", "w", encoding="utf-8")
for i in range(1, 11):
    f04.write(f"{i}번째 줄입니다. \n")
f04.close()

f04 = open("basic01/new-file02.txt", "r", encoding="utf-8")
content = f04.read()
print(content)
f04.close()

