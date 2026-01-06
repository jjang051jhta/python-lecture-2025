import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

netflix = pd.read_csv("./netflix_data_analysis/netflix_titles.csv")
# print(netflix.head())
# print(netflix.tail())
# print(netflix.info())
for idx in netflix.columns :
  missingValueRate = netflix[idx].isna().sum() / len(netflix)*100
  if missingValueRate > 0:
    print(f"{idx} : {round(missingValueRate,2)}%")


netflix["country"] = netflix["country"].fillna("No Data")  #결측치 보정  10% 미만인 country를 No Data로 채움
print("="*100)
for idx in netflix.columns :
  missingValueRate = netflix[idx].isna().sum() / len(netflix)*100
  if missingValueRate > 0:
    print(f"{idx} : {round(missingValueRate,2)}%")
