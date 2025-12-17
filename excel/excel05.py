import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
from pathlib import Path
url = "https://finance.naver.com"
res = requests.get(url)
#print(res.raise_for_status()) # http 제대로 전송되었다면 None 아니면 exception발동
res.raise_for_status()
html = res.text
#print(html)
soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())
tbody =  soup.select_one(".aside_popular table > tbody")
#print(tbody.prettify())
tr_list = tbody.select("tr")
data_list=[]
for tr in tr_list:
  name = tr.select_one("a").get_text(strip=True)
  current_price = tr.select_one("td").get_text(strip=True)
  up_down = tr.select_one("td em.bu_p > .blind").get_text(strip=True)
  change_price = tr.select_one("td .tah").get_text(strip=True)
  data_list.append([name,current_price,up_down,change_price])
print(data_list)
wb = Workbook()
ws = wb.active
ws.column_dimensions["A"].width=20
ws.column_dimensions["B"].width=15
ws.column_dimensions["C"].width=10
ws.column_dimensions["D"].width=15

header = ["주식명","현재가","등락","등락금액"]
ws.append(header)
for data in data_list:
  ws.append(data)
current_dir = Path(__file__).resolve().parent
wb.save(current_dir / "naver_finance.xlsx")