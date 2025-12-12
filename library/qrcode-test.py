# pip install qrcode
import qrcode
from pathlib import Path

qrcode_data = "www.daum.net"
qrcode_img = qrcode.make(qrcode_data)

current_folder = Path(__file__).resolve().parent

save_folder = current_folder / "qrcode"
save_folder.mkdir(exist_ok=True)
save_file_name = save_folder / f"{qrcode_data}.png"


qrcode_img.save(save_file_name)
# quiz 어제 배운 Path를 이용해서 qrcode라는 폴더 만들어서 저장
