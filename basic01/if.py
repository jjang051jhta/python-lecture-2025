money = 3000
card = True
if card or money >= 4800:  # >,<,>=,<=,==,!=  비교연산자
    print("택시 탈 수 있음")
else:
    print("걸어가야함")

isIn = 1 not in [1, 2, 3]
print(isIn)

wallet = ["phone", "card", "money"]
if "phone" in wallet:
    print("택시가능")
else:
    print("걸어가라")
