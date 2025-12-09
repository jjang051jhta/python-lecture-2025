# 1~100 숫자 맞추기
from random import randint  # 기본라이브러리

random_num = randint(1, 100)

game_count = 1

while True:
    try:
        my_num = int(input("1~100사이의 숫자를 쓰세요 : "))
        if my_num > random_num:
            print("다운")
        elif my_num < random_num:
            print("업")
        else:
            print("딩동댕")
            print(f"축하합니다.{game_count}회 만에 맞췄습니다.")
            break
        game_count += 1
    except:
        print("숫자를 입력하세요.")
