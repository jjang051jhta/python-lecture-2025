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
df["ma3"] = df["sales"].rolling(3).mean()
line_color = "#1f77b4"
ma_color = "#ff7f0e"

plt.figure(figsize=(10, 5))

plt.plot(
    df["day"], df["sales"],
    color=line_color,
    linewidth=2,
    marker="o",
    markersize=6,
    markerfacecolor="white",
    markeredgecolor=line_color,
    markeredgewidth=1.5,
    label="Sales"
)

plt.plot(
    df["day"], df["ma3"],
    color=ma_color,
    linewidth=2,
    linestyle="dashed",
    label="MA(3)"
)

# 최대값 표시 + 주석
idx = df["sales"].idxmax()
x_max = df.loc[idx, "day"]
y_max = df.loc[idx, "sales"]
plt.plot([x_max], [y_max], marker="o", markersize=10)

plt.annotate(
    f"MAX {y_max}",
    xy=(x_max, y_max),
    xytext=(x_max - 5, y_max + 8),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Daily Sales Trend", fontsize=14)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.xticks(range(5, 31, 5))
plt.ylim(df["sales"].min() - 10, df["sales"].max() + 10)
plt.grid(True, linestyle="--", alpha=0.5)

plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
plt.tight_layout()
plt.show()
