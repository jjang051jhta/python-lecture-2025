from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = "https://v.daum.net/v/20251216080050633"
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # 브라우져를 띄우지 않음
options.add_argument("--no-sandbox")    # 브라우져를 띄우지 않음
options.add_argument("--disable-gpu")   # 브라우져를 띄우지 않음
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(2)
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source,"html.parser")
recomm_news_list = soup.select(".box_news_recomm .list_column li")
for item in recomm_news_list:
  print(item.get_text(strip=True))