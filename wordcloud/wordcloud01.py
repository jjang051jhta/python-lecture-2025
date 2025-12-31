#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="파이썬 데이터 분석 시각화 라이브러리로는 맷플롯립, 씨본, 플롯리 등이 있다. 판다스는 데이터 분석을 위한 라이브러리이다. 넘파이는 수치해석을 위한 라이브러리이다. 사이킷런은 머신러닝을 위한 라이브러리이다. 텐서플로우와 케라스는 딥러닝을 위한 라이브러리이다. 장고와 플라스크는 웹 개발을 위한 프레임워크이다. "
wd =  WordCloud(font_path="C:\Windows\Fonts\malgun.ttf", 
                width=1200, 
                height=800, 
                background_color="white",
                stopwords={"파이썬", "위한", "라이브러리이다"}
                )
img = wd.generate(text)
plt.imshow(img)
plt.axis("off")
plt.show()