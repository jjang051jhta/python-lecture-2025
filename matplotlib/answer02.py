import pandas as pd
import matplotlib.pyplot as plt

data = {
"day":list(range(1,31)),# 1일 ~ 30일
"sales": [
120,130,125,140,150,155,160,
158,162,170,180,175,178,182,
190,200,195,198,205,210,
215,220,218,225,230,
235,240,238,242,250
    ]
}

df = pd.DataFrame(data)
first_day =  df.loc[df["sales"] >=200,"day"].iloc[0]
df02 = df[df["day"] >= first_day]
plt.plot(df02["day"], df02["sales"])
plt.show()