from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.daum.net")
time.sleep(2)
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("파이썬")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
