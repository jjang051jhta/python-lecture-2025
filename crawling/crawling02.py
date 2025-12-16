from bs4 import BeautifulSoup
import requests
# pip install requests
#외부 요청을 보내기 위해서 requests를 설치
url = "https://v.daum.net/v/20251216080050633"
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html,"html.parser")
#print(soup.select_one(".tit_view").get_text())
#print(soup.select(".article_view strong"))
sub_list = soup.select(".article_view strong")
for item in sub_list:
  print(item.text)

# recomm_news_list = soup.select(".box_news_recomm .list_column li")
# print(recomm_news_list)
#pip install selenuim
# selenium은 브라우져 제어가 가능