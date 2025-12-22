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
#print(df)
plt.figure()
df["ma3"] = df["sales"].rolling(3).mean()
print(df["ma3"])

print('df["sales"].cummax()===',df["sales"].cummax())
plt.plot(df["day"],df["sales"], color="#1f77b4", linewidth=1, linestyle="dashed", 
         marker="o", 
         markersize=4,
         markerfacecolor="#ffffff", 
         markeredgecolor="#004155",
         markeredgewidth=1.5,
         label="sales"
         )
plt.plot(df["day"],df["sales"].cummax(),label="cummax",color="#fd0e0e",linestyle="dashed")
plt.plot(df["day"],df["ma3"],label="MA(3)",color="#05b42b",linestyle="dashed")
plt.title("Daily Sales Trend", fontsize=16, fontweight="bold", color="#04b6ec", 
          loc="center", pad=20)
#print(df["sales"].min(),df["sales"].max())
plt.ylim(df["sales"].min()-10,df["sales"].max()+10)
plt.xticks(range(1,32,2))
plt.grid(True, linestyle="dotted")
plt.legend()
print("=="*60)
#print(df["sales"] >=200)
plt.figure()
print(df.loc[df["sales"] >=200,"day"].iloc[0])
first_day =  df.loc[df["sales"] >=200,"day"].iloc[0]
df02 = df[df["day"] >= first_day]
plt.plot(df02["day"], df02["sales"])
plt.show()



