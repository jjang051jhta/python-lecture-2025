import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

np.random.seed(0)
height = np.random.normal(170,10,100)
weight = height*0.9+np.random.normal(0,2,100)
plt.scatter(height,weight,alpha=0.75, s=36)  #s=36이 default
plt.show()