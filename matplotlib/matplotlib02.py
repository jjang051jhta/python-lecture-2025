# 시각화는 표그리기  matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0,10,100)
y1= x
y2=x*2
y3= x*0.5
y4 = x*3
plt.plot(x,y1,label="y=x")
plt.plot(x,y2,label="y=2x")
plt.plot(x,y3,label="y=0.5x")
plt.plot(x,y4,label="y=3x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("line chart")
plt.show()
