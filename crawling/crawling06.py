from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
webdriver.Chrome(options=options)
wait = WebDriverWait(driver,10)
driver.get("https://www.youtube.com")
wait.until(EC.presence_of_element_located((By.NAME,"search_query")))
search_box = driver.find_element(By.NAME,"search_query")
search_box.send_keys("golden")
search_box.send_keys(Keys.ENTER)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"ytd-video-renderer")))
soup = BeautifulSoup(driver.page_source,"html.parser")
videos = soup.select("ytd-video-renderer")
for idx,video in enumerate(videos,1):
  title =  video.select_one("#video-title").get_text(strip=True)
  channel =  video.select_one("#text-container").get_text(strip=True)
  print(f"{idx}. 제목 : {title} / 채널 : {channel}")
driver.quit()