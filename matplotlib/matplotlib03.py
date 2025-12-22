# 시각화는 표그리기  matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,6))
plt.plot([1,2,3,4],[3,6,9,12])
plt.xlabel("x")
plt.ylabel("y")
# plt.xlim([0,5])
# plt.ylim([0,15])
plt.axis([0,5,0,15])  #한번에 쓰기
plt.title("line chart")
plt.show()
