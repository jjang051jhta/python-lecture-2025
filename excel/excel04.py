# pip install selenium
# pip install beautifulsoup4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from openpyxl import Workbook, load_workbook
from pathlib import Path

current_dir =  Path(__file__).resolve().parent

driver = webdriver.Chrome() 
wait = WebDriverWait(driver,10)
driver.get("http://www.daum.net")
wait.until(
  EC.presence_of_all_elements_located
  ((By.CSS_SELECTOR,".board_news .cont_board .list_txt li"))
)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
news_list = soup.select(".board_news .cont_board .list_txt li")

wb =  Workbook()
ws = wb.active
ws.title = "다음 오늘의 주요 뉴스"
ws.append(["번호","제목","바로가기"])
for idx, item in enumerate(news_list, start=1):
  a=item.select_one("a")
  title = a.get_text(strip=True)
  link = a.get("href","")
  ws.append([idx,title,link])

#save_excel =  current_dir / "daum_news.slsx"
wb.save(current_dir / "daum_news.xlsx")