# 결측치  NaN, None  100000000   짜장면이 좋다  80000000
# 5%미만이면 버리기
# 5~20% 평균값 입력, 중간값 입력을 한다.
# 20%이상이면  행을 삭제
import pandas as pd  #주로 표를 다룰때 쓴다 csv, excel, sql 테이블
import numpy as np
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)
netflix_csv = pd.read_csv("./pandas/netflix.csv")
isna_sum = netflix_csv.isna().sum()
print(isna_sum)
print(netflix_csv.info())