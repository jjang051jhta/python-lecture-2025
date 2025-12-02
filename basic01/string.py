name = "장성호"
print(name)
name = '장성호'
print(name)
say = """Life is short,
You need python
"""
say = "Life's short,You need python"
print(say)
print("="*50)
print("author : jjang051")
print("="*50)
print(len(say))
print(say[0])
print(say[1])
print(say[2])
print(say[-1])
print(say[0:])
dateStr = "20251201Rainy"  #날짜랑 날씨 뽑아보기  
date = dateStr[0:8]
weather = dateStr[8:]
print(f"{date}:{weather}")
#dateStr[1] = "f"
print(f"{'hi':>10}")
print(f"{'hi':<10}")
print(f"{'hi':^10}")
print(f"{'hi':-^20}")
print(f"{7:0>8}")
print(f"{1234567:0>12,}")
#count("문자")  문자의 빈도 수 
print(say.count("s"))  #count는 특정 글자의 빈도 수
print(say.count("X"))  #count는 특정 글자의 빈도 수

#find("문자")  해당하는 문자의 index 없으면 -1을 리턴
print("say.find('s')",say.find("s"))

#index("문자")  해당하는 문자의 index 없으면 오류
print("say.index('s')",say.index("s"))

#print("say.index('b')",say.index("b"))

#'문자'.join("문자열") 해당하는 문자열을 문자를 삽입해준다.
print("','.join(say)",','.join(say))
str01 = "   hi"
print(str01.lstrip())
str01 = "   hi     "
print(str01.rstrip())
print(str01.strip())

str02 = "Life is too short"
print(str02.replace("Life","Your leg"))
str03 = "Life"
print("str03.isalpha()",str03.isalpha())
str04 = "12345"
print("str04.isdigit()",str04.isdigit())
str05 = "Python3"
print("str05.isalnum()",str05.isalnum()) #문자와 숫자만 허용 특수문자는 안됨
str06 = "    "
print("str06.isspace()",str06.isspace()) #공백만 있으면 True
str07 = "life is too short"
print("str07.lower()",str07.lower())
print("str07.upper()",str07.upper())
print("str07.capitalize()",str07.capitalize())
print("str07.title()",str07.title())







a=10
b=5
a,b = b,a
print(a,"===",b)

