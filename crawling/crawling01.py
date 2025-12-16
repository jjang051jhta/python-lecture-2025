# pip install beautifulsoup4
from bs4 import BeautifulSoup as bs #데이터 추출할때
#print(dir(bs))
html ="""
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
soup01 = bs(html, "html.parser")  #html.parser를 쓰면 html을 파싱해준다.
#print(soup01)
#print(soup01.find("h1").text)  #간단한 텍스트 출력
#print(soup01.find("h1").get_text(strip=True, separator="/"))
#print(soup01.find("li").get_text()) # find는 처음 발견한 것 하나만 들고 온다.
li_list = soup01.find_all("li")
for item in li_list:
  print(item.get_text())

# find는 태그 기반
# select는 css 기반  복잡한거 찾을 때 좋음...
print(soup01.find("h1",{"id":"another-title"}).text)
print(soup01.select_one("#another-title").text)
li_list02 = soup01.select(".menu")
for item in li_list02:
  print(item.get_text())


#find("태그네임"), find_all("태그네임")
#select_one("css 선택자"), select("css 선택자")