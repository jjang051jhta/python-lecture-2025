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
  wait = WebDriverWait(driver,10)
  wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                         'img[data-testid="asset-grid-masonry-img"]'))
  )
  soup = BeautifulSoup(driver.page_source,"html.parser")
  imgs =  soup.select('img[data-testid="asset-grid-masonry-img"]')
  folder = Path(f"unsplash_imges_{search}")
  folder.mkdir(parents=True,exist_ok=True)
  print(len(imgs))
  count= 0
  src_list =[]
  #print(imgs[0].get("src"))
  for img in imgs:
    src = img.get("src")
    if not src:
      continue
    if count>=total:
      break
    src_list.append(src)
    count+=1
  #print(soup.prettify())
  #print(src_list)
unsplash_img_crawling()