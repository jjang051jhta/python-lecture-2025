# pip install beautifulsoup4
from bs4 import BeautifulSoup
html="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1 id="title">
      <span>파이썬</span>
      <b>크롤링</b>
    </h1>
    <h1 id="another-title">이것도 타이틀</h1>
    <ul class="menu">
      <li>뉴스</li>
      <li>블로그</li>
      <li>카페</li>
    </ul>
  </body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")
print(soup.find("h1").text)
print(soup.find("h1").get_text(strip=True, separator="/"))
h1_list = soup.find_all("h1")
menu_list = soup.find_all("li")
print(h1_list)
print(h1_list[0].text)
print(h1_list[1].text)
print(menu_list)
menu_list02 = soup.select(".menu > li")
print(menu_list02)
print(menu_list02[0].text)
menu_list03 = soup.select_one(".menu > li")
print(menu_list03)
print(menu_list03.text)

import requests
url = "https://v.daum.net/v/20251217094503297"
html02 = requests.get(url)
#print(html02.text)
soup02 = BeautifulSoup(html02.text,"html.parser")
#print(soup02.prettify())
title = soup02.select_one("h3.tit_view")
print(title.text)

