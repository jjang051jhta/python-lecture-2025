from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.daum.net")
time.sleep(2)
print(driver.title)
print(driver.page_source)
driver.quit()
#back을 rest vs front에 리액트 써서 렌더링