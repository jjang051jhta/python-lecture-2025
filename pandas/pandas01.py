#pandas는 표을 다루는 라이브러리
# pip install pandas
import pandas as pd  #주로 표를 다룰때 쓴다 csv, excel, sql 테이블
import numpy as np
#시리즈: 1차원 배열, 인덱스가 붙어있음
#데이터프레임: 2차원 배열, 행과 열로 구성, 인덱스와 컬럼명이 붙어있음
series_data = pd.Series([True,3.14,"ABC"])
print(type(series_data))
print(series_data)
df = pd.DataFrame({"c0":[1,2,3],"c1":[4,5,6],"c2":[7,8,9]})
print(type(df))
print(df)

dict_netflix = {
    'title':['Squid Game', 'Stranger Things', 'Sherlock Holmes', 'Iron Man & Captain America: Heroes United', 'Bird Box', 'Anne with an E', 'About Time','Inception'],
    'director':[np.nan, np.nan, 'Guy Ritchie', 'Leo Riley', 'Susanne Bier', np.nan, 'Richard Curtis', 'Christopher Nolan'],
    'cast':['Lee Jung-jae', 'Winona Ryder', 'Robert Downey Jr', 'Adrian Pasdar', 'Sandra Bullock','Amybeth McNulty', 'Domhnall Gleeson', 'Leonardo DiCaprio'],
    'country':[np.nan, 'United States', 'United States, Germany', 'United States', 'United States', 'Canada', np.nan, 'United States'],
    'release_year':[2021, 2019, 2009, 2014, 2018, 2019, 2013, 2010],
    'duration':[300, 800, 128, 71, 124, 900, 123, 148],
    'listed_in':[np.nan, 'TV Horror', 'Action & Adventure', np.nan, np.nan, np.nan,np.nan, np.nan]}
#netflix = pd.DataFrame(dict_netflix)
#print(netflix)

netflix_csv = pd.read_csv("./pandas/netflix.csv")
#netflix_csv.to_csv("./pandas/netflix_out.csv", index=False)

print(f"netflix_csv.columns={netflix_csv.columns}")
print(f"netflix_csv.index={netflix_csv.index}")
print(f"netflix_csv.index={list(netflix_csv.index)}")
netflix_csv.index = ["1행", "2행", "3행", "4행", "5행", "6행", "7행", "8행"]
#print(netflix_csv.loc[2])
print(netflix_csv.loc["3행"])



