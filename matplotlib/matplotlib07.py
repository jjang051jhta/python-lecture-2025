import matplotlib.pyplot as plt
import numpy as np
labels = ["A","B","C"]
x = np.arange(len(labels))
print(x)
y1=[10,20,30]
y2=[15,18,35]
plt.barh(x,y1,label="2024", zorder=3)
plt.barh(x,y2,left=y1,label="2025", zorder=3)
plt.yticks(x, labels)
plt.grid(axis="y",linestyle="--", alpha=0.5)
plt.legend()
plt.show()  

#grid넣고 yaxis를 높여서 글자가 벗어나지 않게