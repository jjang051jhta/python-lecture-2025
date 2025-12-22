import pandas as pd
from pathlib import Path
curernt_dir = Path(__file__).resolve().parent
netflix_csv = pd.read_csv(curernt_dir / "netflix.csv")
print("mean :",netflix_csv["duration"].mean())
print("median :",netflix_csv["duration"].median())
print("sum :",netflix_csv["duration"].sum())
print("min :",netflix_csv["duration"].min())
print("max :",netflix_csv["duration"].max())
#표준편차 는 var를 류트 씌운거
print("std :",netflix_csv["duration"].std())  
#분산(var)  값들이 평균에서 얼마나 흩어져 있는지를 제곱을 해서 계산
print("var :",netflix_csv["duration"].var())  
# 70,80,90  
# 평균 80
# 분산  (70-80)**2+(80-80)**2+ (90-80)**2 =200 / 3 분산
# 표준편차  분산값을 루트 
#mean을 기준으로 해서 좌주 324 정도  좌우로 펼쳐져 있다.
print("count :",netflix_csv["type"].count())  #결측치는 제외  NaN이 있으면 제외
print("value_count :",netflix_csv["type"].value_counts(dropna=False))  
print(netflix_csv[["release_year","duration"]].describe())
print(netflix_csv.agg({"release_year":["min","max","median","std","mean"],
                       "duration":["min","max","median","std"]
                       }))
