from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.gmarket.co.kr/")
time.sleep(2)
superdeal = driver.find_element(By.CSS_SELECTOR,'a[data-montelena-service="슈퍼딜"]')
superdeal.click()
time.sleep(3)
