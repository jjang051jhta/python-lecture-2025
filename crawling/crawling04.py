from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)  #최대 10초대기
driver.get("https://www.naver.com")
# time.sleep(2)  # 2초 
search_box = wait.until(
  EC.presence_of_element_located((By.CLASS_NAME,"search_input"))
)

#search_box = driver.find_element(By.CLASS_NAME,"search_input")
search_box.send_keys("영화")
search_box.send_keys(Keys.ENTER)
# time.sleep(3) # 정확하게 3초 대기  1초만에 파싱
wait.until(
  EC.presence_of_element_located((By.CLASS_NAME,"card_area"))
)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())
card_items = soup.select(".card_area .card_item")
for item in card_items:
  print(item.select_one(".this_text").get_text())