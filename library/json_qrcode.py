import json
import qrcode
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).resolve().parent
json_path = current_dir / "qrcode.json"
logo_dir = current_dir / "logo"
output_dir = current_dir / "qrcode"

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
# dictionary, tuple,list <=> json
with open(json_path, "r", encoding="utf-8") as f:
    items = json.load(f)
# print(items)


def create_qrcode(url: str, logo_name: str, output: Path):
    qr = qrcode.QRCode(
        version=6,  # 가로세로 셀(cell) 숫자  6 = 41
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,  # 하나의 cell 크기
        border=4,  # qr의 크기는 version의 숫자에 해당하는 cell 숫자 * box_size로 이루어 진다.
    )
    qr.add_data(url)
    qr.make(
        fit=True
    )  # 크기를 바꿔주는 옵션  만약 qr을 만드는 data가 qrcode크기보다 크다면 version을 바꿔서 크기를 자동으로 키워라
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_width, qr_height = qr_img.size  # 가로 세로 크기가 tutple로 나온다.
    logo_path = logo_dir / logo_name
    if not logo_path.exists():
        print(f"로고 파일 없음 : {logo_path.name}")
        return
    logo = Image.open(logo_path).convert("RGBA")
    logo_size = qr_width // 5
    logo = logo.resize((logo_size, logo_size))
    center_position = (
        (qr_width - logo_size) // 2,
        (qr_height - logo_size) // 2,
    )
    qr_img.paste(logo, center_position, logo)
    qr_img.save(output, format="PNG")
