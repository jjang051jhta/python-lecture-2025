import matplotlib.pyplot as plt
categories = ["A","B","C","D"]
values = [10,25,15,30]
plt.bar(categories,values, 
        color="#ff0000", edgecolor="#000000", linewidth=2,
        width=0.6
        )
for i, value in enumerate(values):
  plt.text(i,value, str(value), ha="center", va="bottom",color="#000000")
"""
plt.barh(["A","B","C","D"],[10,25,15,30], 
        color="#ff0000", edgecolor="#000000", linewidth=2,
        height=0.8
        )
        """    
#plt.plot() 은 선그래프
# bar는 세로 막대(width) barh는 가로막대 (height) 사용
plt.show()