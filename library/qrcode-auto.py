import qrcode
from pathlib import Path

current_folder = Path(__file__).resolve().parent
save_folder = current_folder / "qrcode-auto"
save_folder.mkdir(exist_ok=True)
txt_path = current_folder / "qrcode.txt"
with open(txt_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
# print(lines)
for url in lines:
    if not url.strip():
        continue
    file_name = url.replace("www.", "") + ".png"
    save_path = save_folder / file_name
    qrcode_img = qrcode.make(url)
    qrcode_img.save(save_path)
print("qrcode 생성완료")
