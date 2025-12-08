# f = open("basic01/review/new-file.txt", "w", encoding="utf-8")
# f.write("hello python!!")
# f.close()

# python안에는 기본 모듈이 있다. 필요하면 가져다 쓰면 된다.
# import 통해서 가져다 쓰면 된다.
# 만약 기본라이브러리가 아니라면 pip install을 통해서 설치해야 한다.
import os

folder_name = "review"
os.makedirs(folder_name, exist_ok=True)
file_path = os.path.join(folder_name, "new-file.txt")
# 파일을 열때 w는 쓰기모드, r은 읽기 모드, a 는 기본 글에 덧붙이기
f = open(file_path, "w", encoding="utf-8")
f.write("hello python!!")
f.close()
# 날짜별 폴더를 만들어야 한다.

f02 = open("review/new-file.txt", "r", encoding="utf-8")
content = f02.read()
print(content)
f02.close()

with open("basic01/scores.txt", "r", encoding="utf-8") as f03:
    while True:
        line = f03.readline()
        if not line:
            break
        print(line)
with open("basic01/scores.txt", "r", encoding="utf-8") as f04:
    total = 0
    count = 0
    for line in f04:
        name, score = line.strip().split()
        total += int(score)
        count += 1
    print(total / count)
