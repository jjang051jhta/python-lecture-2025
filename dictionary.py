# list       ===  list
# tuple      ===  list (불변)
# dictionary ===  map

dic = {"name": "장성호", 
       "phone": "010-1111-1111", 
       "age": 20, 
       1: "001",
       "name":"장동건"
       } # fmt: skip
print(dic)
print(dic["name"])
print(dic[1])
dic["email"] = "jjang051@hanmil.net"
print("email===", dic.get("mail"))  # get(key)는 값이 없으면 None 리턴
# print("email===", dic["mail"])  # 오류
mail = dic.get("mail", "noname@xxx.com")
print("mail===", mail)
email = dic.pop("email")  # pop은 키값을 제거하면서 값을 가져온다.
print("email===", email)
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
for key in dic.keys():
    print(key)
