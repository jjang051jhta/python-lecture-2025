import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
from pathlib import Path

def is_mean_td(tr):
  tds = tr.select("td")
  if not tds:
    return False
  if len(tds) <= 1:
    return False
  return True

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = requests.get(url)
res.raise_for_status()
html = res.text
soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())
table = soup.select_one("#contentarea .box_type_l table")
#print(table.prettify())
tr_list = table.select("tr")
data_list = []
rows = []
for tr in tr_list:
  if not is_mean_td(tr):
    continue
  #print(tr)
  td_list = tr.select("td")
  #print(td_list)
  row = []
  for td in td_list:
    row.append(td.get_text(strip=True))
  rows.append(row)
#print(rows)  
wb = Workbook()
ws = wb.active
ws.title="인기주식30"

header = ["순위",	"종목명",	"검색비율","현재가",	"전일비",	"등락률",	"거래량",	"시가",	"고가",	"저가",	"PER"]
ws.append(header)
for row in rows:
  ws.append(row)
current_dir = Path(__file__).resolve().parent
wb.save(current_dir / "naver_popular.xlsx")  

  



