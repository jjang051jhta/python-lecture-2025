import json
from pathlib import Path

current_dir = Path(__file__).resolve().parent
json_path = current_dir / "qrcode.json"

dic = [
    {"url": "www.coupang.com", "logo": "logo05.png", "name": "쿠팡"},
    {"url": "www.coupang.com", "logo": "logo05.png", "name": "쿠팡"},
    {"url": "www.coupang.com", "logo": "logo05.png", "name": "쿠팡"},
    {"url": "www.coupang.com", "logo": "logo05.png", "name": "쿠팡"},
]
# nums = [1, 2, 3, 4, 5]
# json_data = json.dumps(dic, ensure_ascii=False, indent=2)
# json_data = json.dumps(nums, ensure_ascii=False, indent=2)
# json_data = json.dumps((1, 2, 3, 4, 5), ensure_ascii=False, indent=2)
# print(json_data)

with open(json_path, "r", encoding="utf-8") as f:
    items = json.load(f)
# print(items)
# dictionary, tuple,list <=> json
