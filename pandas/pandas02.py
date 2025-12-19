import pandas as pd  #주로 표를 다룰때 쓴다 csv, excel, sql 테이블
import numpy as np
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)
netflix_csv = pd.read_csv("./pandas/netflix.csv")
#print(netflix_csv)
#print(netflix_csv.title)
#print(netflix_csv[["title","director"]])
#print(netflix_csv.release_year > 2015)
#netflix_2015_later = netflix_csv[netflix_csv.release_year>2015]
#netflix_2015_later = netflix_csv[netflix_csv["release_year"]>2015]
#print(netflix_2015_later)
#netflix_2015_before = netflix_csv[netflix_csv["release_year"] < 2015]
#netflix_2015_before = netflix_csv[~(netflix_csv["release_year"] > 2015)]
#print(netflix_2015_before)
# netflix_2015_later_tvshow = netflix_csv[(netflix_csv["release_year"] > 2015) & 
#                                  (netflix_csv["type"]=="TV Show")]
# print(netflix_2015_later_tvshow)
# netflix_2015_later_or_tvshow = netflix_csv[(netflix_csv["release_year"] > 2015) |
#                                  (netflix_csv["type"]=="TV Show")]
# print(netflix_2015_later_or_tvshow)
#loc()
#title_year = netflix_csv.loc[0:3,["title","release_year"]]   #loc는 컬럼명으로 접근
#title_year = netflix_csv.loc[[0,1,2,3],["title","release_year"]] 
title_year_iloc = netflix_csv.iloc[[3,4],[1,3]] #iloc는 index로 접근
print(title_year_iloc)
print(netflix_csv["type"].isin(["TV Show"]))
#only_tvshow = netflix_csv[netflix_csv["type"].isin(["TV Show"])]
only_tvshow = netflix_csv[netflix_csv["type"]=="TV Show"]
print(only_tvshow)

