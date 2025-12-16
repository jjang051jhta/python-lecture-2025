from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from pathlib import Path
def unsplash_img_crawling(search="nature", total=10):
  options = Options()
  options.add_experimental_option("detach",True)
  driver = webdriver.Chrome(options=options)
  wait = WebDriverWait(driver,10)
  url = f"https://unsplash.com/s/photos/{search}"
  driver.get(url)

unsplash_img_crawling()