# 1. " Python Developer " 문자열에서 앞뒤 공백을 제거하여 출력하세요.
print(" Python Developer ".strip())
# 2. "hello WORLD" 를 모두 대문자로 변환하여 출력하세요.
print("hello WORLD".upper())
# 3. "hello WORLD" 를 모두 소문자로 변환하여 출력하세요.
print("hello WORLD".lower())
# 4. "python programming" 문장에서 "programming"을 "algorithm"으로 변경하여 출력하세요.
print("python programming".replace("programming","algorithm"))
# 5. "Data-Engineer" 에서 "-" 를 "_" 로 변경해 출력하세요.
print("Data-Engineer".replace("-","_"))
#6. "Busan Harbor" 가 "Busan" 으로 시작하는지 검사하여 출력하세요.
print("Busan Harbor".startswith("Busan"))
#7. "cloud-service.org" 가 ".org" 로 끝나는지 검사하여 출력하세요.
print("Busan Harbor".endswith(".org"))
#8. "JavaToPython" 문자열에 "Python"이 포함되어 있는지 True/False로 출력하세요.
print(f"{'Python' in 'JavaToPython'}")
#9. "security_patch_v5" 문자열에서 "patch" 의 시작 위치 인덱스를 출력하세요.
print("security_patch_v5".find("patch"))
#10. "DeepLearning" 문자열 길이를 출력하세요.
print(len("DeepLearning"))
#11. "API_ERROR_404" 에서 "ERROR" 를 "error" 로 변경해 출력하세요.
print("API_ERROR_404".replace("ERROR","error"))
print(f"{'API_ERROR_404'.replace('ERROR','error')}")
#12. " Tokyo Night View" 문자열에서 왼쪽 공백만 제거해 출력하세요.
print(f"{' Tokyo Night View'.lstrip()}")
#13. "Seoul " 문자열에서 오른쪽 공백만 제거해 출력하세요.
print(f"{'Seoul '.rstrip()}")
#14. "FastAPI" 를 폭 12, 가운데 정렬로 출력하세요.
print(f"{'FastAPI':^12}")
#15. "debug_mode" 에서 "mode" 를 "LEVEL" 로 변경해 출력하세요.
print(f"{'debug_mode'.replace('mode','LEVEL')}")
#16. "Python3.12.1" 에서 . 을 제거한 뒤 영문/숫자만 남았는지 검사하여 출력하세요.
str =  "Python3.12.1".replace(".","")
print(f"{str}")
print(f"{str.isalnum()}")
#17. "Pyramid" 문자열을 뒤집어서 출력하세요.
print(f"{'Pyramid'[::-1]}")
print(f"{'Pyramid'[::-1]}")
#18. "Hello\nPython" 에서 줄바꿈 \n 을 공백 " "으로 변경해 출력하세요.
print(f"{'Hello\nPython'.replace('\n'," ")}")
#19. "alphaNUM123" 의 대소문자를 서로 반대로 변경해 출력하세요.
print(f"{'alphaNUM123'.swapcase()}")
#20. "Google Search Console" 을 타이틀 케이스로 변환하여 출력하세요.
print(f"{'google search console'.title()}")
print(f"{'google search console'.capitalize()}")
#21. "password=1234;" 에서 = 의 인덱스 위치를 출력하세요.
print(f"{'password=1234;'.find('=')}")
#22. "http://localhost" 가 "https" 로 시작하는지 검사하여 출력하세요.
print(f"{'http://localhost'.startswith('http')}")
#23. "__init__method" 에서 "method" 의 시작 인덱스를 출력하세요.
print(f"{'__init__method'.find('method')}")
#24. "CamelCASEstring" 이 영문/숫자만으로 구성되어 있는지 검사하여 출력하세요.
print(f"{'CamelCASEstring'.isalnum()}")
#25. "ErrorWarningCritical" 에서 "Warning" 시작 인덱스를 출력하세요.
print(f"{'ErrorWarningCritical'.find('Warning')}")
#26. "Python_SCRIPT" 에서 "_" 뒤 문자열만 소문자로 출력하세요.
print(f"{'Python_SCRIPT'.split('_')[1].lower()}")
#27. "MachoCulture" 에서 "Culture" 를 "CULTURE" 로 변경해 출력하세요.
print(f"{'MachoCulture'.replace('Culture','CULTURE')}")
#28. "EncodingTest" 에서 "Test" 가 처음 나오는 인덱스를 출력하세요.
print(f"{'EncodingTest'.find('Test')}")
#29. 문자열을 입력받아 "start" 로 시작하면 "yes", 아니면 "no" 출력하세요.

str =  input("문자열 입력 : ")
#if str.startswith("start") :  
#  print("yes")
#else :
#  print("no")
#삼항연산자 조건 ? a : b 파이썬에는 없다.
result = "yes" if str.startswith("start") else "no";
print(result)

