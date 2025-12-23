# 시각화 라이브러리 matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16], label="y=x**2", 
         marker="o", markersize=8,markerfacecolor="#ffffff", 
         color="#12db00",
         markeredgecolor="blue",
         markeredgewidth=2
         )
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.title("Line Chart", 
          fontsize=18, 
          fontweight="bold",
          color="#ff0000",
          loc="center", #left, center, right  
          pad=10
          )
plt.minorticks_on()
plt.legend(loc="upper center", fontsize=10, title="line type",title_fontsize=12)
plt.grid(True, alpha=0.5, which="major")
plt.grid(True, alpha=0.3, which="minor", linestyle="dotted")
#plt.axis([0,5,0,17])
plt.xlim(0,5)
plt.ylim(0,17)
plt.show()