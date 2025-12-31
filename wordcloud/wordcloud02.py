from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import pandas as pd
#pip install pillow
from PIL import Image
import numpy as np

netflix = pd.read_csv("./netflix_preprocessed.csv", encoding="utf-8")
#text = str(list(netflix["description"]))
text = " ".join(netflix["description"].dropna().astype(str))
mask = np.array(Image.open("./netflix_logo.jpg"))
#print(netflix.head())
#print(text)
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("", ["#4b4b4b", "#b20710"])
stopwords = set(STOPWORDS)
stopwords.update(["series", "season", "seasons", "will", "one", "new", "also", "many", "most", "some", "us", "about", "after", "more"]) 
print(stopwords)
wd =  WordCloud(
                width=1200, 
                height=800, 
                background_color="white",
                mask=mask,
                colormap=cmap,
                max_words=200,  # 많이 나오는 빈도수 상위 300개만 사용
                min_font_size=16,
                stopwords=stopwords
                #stopwords={"the", "and", "of", "to", "in", "a", "is", "for", "with", "on", "as", "its", "an", "by", "that", "at"} 
                )
img = wd.generate(text)
plt.figure(figsize=(16,8))
plt.imshow(img)
plt.axis("off")
plt.show()

