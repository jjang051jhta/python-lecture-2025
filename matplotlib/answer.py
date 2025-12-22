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
print(df["day"],"===",df["sales"])

plt.plot(df["day"],df["sales"], color="#1f77b4", linewidth=1, linestyle="dashed", 
         marker="o", 
         markersize=4,
         markerfacecolor="#ffffff", 
         markeredgecolor="#004155",
         markeredgewidth=1.5
         )
plt.title("Daily Sales Trend", fontsize=16, fontweight="bold", color="#04b6ec", 
          loc="center", pad=20)
plt.show()

