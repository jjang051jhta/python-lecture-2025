# 날짜 수학관련 기본 라이브러리와 외부 라이브러리
# from datetime import date as d, datetime as dt, time as t
# as 다음에 별명을 쓸 수 있음
from datetime import date, datetime, time, timedelta
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU

d01 = date(2025, 12, 11)
d02 = date(2022, 5, 3)
diff = d01 - d02  # timedelta 생성된다.
print(diff)
print(type(diff))
print(diff.days)
now = datetime.now()
print(now)  # 지금 현재 날짜와 시간
print(f"now.date() : {now.date()}")
today = date.today()  # 날짜만 관여한다.
print(f"date.today() : {date.today()}")
print(f"now.year : {now.year}")
print(f"now.month : {now.month}")
print(f"now.day : {now.day}")
print(f"now.weekday() : {now.weekday()}")  # 월요일(0)~일요일(6)
print(d01 + timedelta(days=365))
print(d01 + relativedelta(years=+10, months=+2, days=+3))
# dateutil,pendulum
next_monday = d01 + relativedelta(weekday=MO(+1))
print(next_monday)
last_day = d01 + relativedelta(day=31)  # relativedelta는 날짜를 자동 보정해준다.
print(last_day)
diff02 = relativedelta(d01, d02)
print(diff02.years, "년", diff02.months, "월", diff02.days, "일")

today = date(2025, 12, 11)
birthday = date(2026, 12, 16)
print(
    relativedelta(birthday, today).years,
    "년",
    relativedelta(birthday, today).days,
    "일",
)
# timedelta는 시간 기반, relativedelta는 달력 기준
print((birthday - today).days)  # 총일수
print(relativedelta(birthday, today).days)  # 년월일 기반
