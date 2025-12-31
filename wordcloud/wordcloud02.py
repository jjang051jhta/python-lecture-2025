from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import pandas as pd
#pip install pillow
from PIL import Image
import numpy as np

netflix = pd.read_csv("./netflix_preprocessed.csv", encoding="utf-8")
text = str(list(netflix["description"]))
mask = np.array(Image.open("./netflix_logo.jpg"))
#print(netflix.head())
#print(text)
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("", ["#4b4b4b", "#b20710"])
wd =  WordCloud(
                width=1200, 
                height=800, 
                background_color="white",
                mask=mask,
                colormap=cmap,
                )
img = wd.generate(text)
plt.imshow(img)
plt.axis("off")
plt.show()

