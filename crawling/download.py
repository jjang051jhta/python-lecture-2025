import requests
from pathlib import Path

def download_image(url:str,save_dir:Path):
  url = url.replace("&amp;","&")
  headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://unsplash.com/",
    }
  img_id =  "001"
  save_path = save_dir / f"{img_id}.jpg"
  with requests.get(url,headers=headers, stream=True, timeout=20) as r:
    r.raise_for_status()
    with open(save_path,"wb") as f:
      for chunk in r.iter_content(chunk_size=8192):
        if chunk:
          f.write(chunk)
download_image("https://images.unsplash.com/photo-1457269449834-928af64c684d?fm=jpg&amp;q=60&amp;w=3000&amp;ixlib=rb-4.1.0&amp;ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2ludGVyfGVufDB8fDB8fHww"
               ,Path(__file__).resolve().parent
               )            