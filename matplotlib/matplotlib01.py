# 시각화는 표그리기  matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16], marker="o",label="y=x²")  #1번째 리스트가 x축 2번째가 y축
plt.xlabel("X Value")
plt.ylabel("X Value")
plt.title("Line Chart")
plt.legend()
plt.grid(True)
plt.show()