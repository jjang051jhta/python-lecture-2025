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

#결측치 비율
for idx in netflix_csv.columns:
  missing_value_rate = netflix_csv[idx].isna().sum() / len(netflix_csv)*100
  if missing_value_rate > 0 :
    print(f"{idx} : null rate = {missing_value_rate}")

print(netflix_csv)
print("="*200)
netflix_csv["country"] = netflix_csv["country"].fillna("No Data")
print(netflix_csv)
print("="*200)
netflix_csv["director"] = netflix_csv["director"].replace(np.nan,"No Name")
print(netflix_csv)
print("="*200)
netflix_csv.dropna(axis=1,inplace=True)  #na가 있으면 삭제해라
print(netflix_csv)
netflix_csv.to_csv("./pandas/netflix_csv_cleaned.csv",index=False)

