# pip install pandas
import pandas as pd
from pathlib import Path
# 한줄일때는 Series
# 행과 열이 있을때는 DataFrame
series_data = pd.Series([True,3.14,"abc", 10])
print(series_data)
data_frame_data = pd.DataFrame({"C0":[1,2,3],"C1":[4,5,6],"C2":[7,8,9]})
print(data_frame_data)
curernt_dir = Path(__file__).resolve().parent
netflix_csv = pd.read_csv(curernt_dir / "netflix.csv")
print(netflix_csv)
print("==="*60)
print(netflix_csv.columns)
print(netflix_csv.index)
print(list(netflix_csv.index)) # index의 값을 list로 바꿔서 출력
print(netflix_csv.loc[0]) #loc를 이용하면 해당하는 행의 값을 뽑을 수 있다.
print(netflix_csv.loc[0,"title"]) #loc[index,컬럼명]를 이용하면 해당하는  특정 컬럼값을 값을 뽑을 수 있다.
print(netflix_csv.loc[[0,4]])
print(netflix_csv.loc[0:4])  #loc는 label 기준 iloc 는 행번호 기준
print("==="*60)
print(netflix_csv.iloc[0:5]) 
new_index_netflix = netflix_csv.set_index("show_id")
print("==="*60)
print(new_index_netflix) #숫자로된 index는 사라지고 show_id가 새로운 인덱스로 바뀜
#print(new_index_netflix.loc[1])
#print(netflix_csv.loc[0])
#netflix_csv.index=["1행","2행","3행","4행","5행","6행","7행","8행"]
#print(netflix_csv)  #오라클 시퀀스 개념이랑 비슷, 고유번호는 따로 존재
# print(netflix_csv.loc["3행","title"])
# print(netflix_csv.loc["3행"]["title"])
print(netflix_csv.head())
print(netflix_csv.tail())
more2015 = netflix_csv[netflix_csv["release_year"] > 2015]
less2015 = netflix_csv[~(netflix_csv["release_year"] > 2015)]
print(more2015)
print(less2015)