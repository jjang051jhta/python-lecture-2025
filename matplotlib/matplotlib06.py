import matplotlib.pyplot as plt
import numpy as np
labels = ["A","B","C"]
x = np.arange(len(labels))
print(x)
y1=[10,20,30]
y2=[15,18,35]
plt.bar(x-0.2,y1,width=0.4,label="2024", zorder=3)
plt.bar(x+0.2,y2,width=0.4,label="2025", zorder=3)

for i, value in enumerate(y1):
  plt.text(x[i]-0.2, value+0.5, str(value), ha="center",va="bottom")

for i, value in enumerate(y2):
  plt.text(x[i]+0.2, value+0.5, str(value), ha="center",va="bottom")


plt.xticks(x, labels)
plt.grid(axis="y",linestyle="--", alpha=0.5)
plt.legend()
max_value = max(max(y1), max(y2))
plt.ylim(0,max_value+5)
plt.show()

#grid넣고 yaxis를 높여서 글자가 벗어나지 않게