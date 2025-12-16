from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

from pathlib import Path

def download_image(url:str,save_path:Path):
  url = url.replace("&amp;","&")
  headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://unsplash.com/",
    }
  with requests.get(url,headers=headers, stream=True, timeout=20) as r:
    r.raise_for_status()
    with open(save_path,"wb") as f:
      for chunk in r.iter_content(chunk_size=8192):  #  8kb 씩 받아라..
        if chunk:
          f.write(chunk)

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
  folder = Path(f"unsplash_images_{search}")
  folder.mkdir(parents=True,exist_ok=True)
  print(len(imgs))
  count= 0
  src_list =[]
  #print(imgs[0].get("src"))
  saved = 0
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
  for src in src_list:
    file_name = f"unsplash_{saved+1:03d}.jpg"
    save_path = folder / file_name
    download_image(src, save_path)
    saved+=1
unsplash_img_crawling("python")