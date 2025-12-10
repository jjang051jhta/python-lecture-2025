# 기본함수는 import 없이 쓸 수 있다.  나머지 필요한것들은 불러다 써야 한다.
from datetime import date, time, timedelta, datetime  # 날짜관련 라이브러리


today = date(2025, 12, 10)
day01 = date(2024, 12, 10)
diff = today - day01  # 연산 가능  timedelta반환
days = ["월", "화", "수", "목", "금", "토", "일"]
print(diff)
print(diff.days)
print(f"today+timedelta(days=7) : {today+timedelta(days=7)}")
print(f"today+timedelta(weeks=2) : {today+timedelta(weeks=2)}")
print(f"today > day01 : {today > day01}")
print(f"today < day01 : {today < day01}")
print(f"today.weekday() : {today.weekday()}")  # 0(월) ~ 6(일)
print(f"today.isoweekday() : {today.isoweekday()}")  # 1(월) ~ 7(일)
print(f"today.weekday() : {days[today.weekday()]}")
now = datetime.now()
today02 = date.today()
print(f"now : {now}")
print(f"today02 : {today02}")
print(f"year : {now.year}")
print(f"month : {now.month}")
print(f"day : {now.day}")
print(f"hour : {now.hour}")
print(f"minute : {now.minute}")
print(f"second : {now.second}")
print(f"format : {now.strftime("%Y-%m-%d %H:%M:%S")}")
now_str = "2025-12-10 11:01:00"
trans_date = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")
print(trans_date)
