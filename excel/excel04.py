# pip install selenium
# pip install beautifulsoup4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
for item in news_list:
  print(item.select_one("a").text)