# PIL 설치 필요
# pip install pillow

import qrcode
from PIL import Image

# QR코드에 넣을 데이터(URL)
data = "www.pixabay.com"

# QRCode 객체 생성
qr = qrcode.QRCode(
    version=4,  # QR 코드 버전(4: 33x33 셀 크기)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # 오류 정정 기능 (H: 약 30%까지 손상 가능)
    box_size=10,  # 한 칸(box)의 픽셀 크기
    border=4,  # 테두리 여백(최소 4)
)

# QR코드에 데이터 추가
qr.add_data(data)
# QR 코드 자동 크기 조절
qr.make(fit=True)

# QR 이미지 생성 (RGBA: 투명도 포함)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# 로고 이미지 경로
logo_path = "./library/logo.png"
logo = Image.open(logo_path)

# 로고 크기 설정 (가운데 넣을 크기)
logo_size = 64

# QR코드의 전체 크기(width, height)
qr_width, qr_height = qr_img.size

# 로고를 QR의 정 중앙에 위치시키기 위한 좌표 계산
logo_position = (
    (qr_width - logo_size) // 2,  # 중앙 정렬된 x좌표
    (qr_height - logo_size) // 2,  # 중앙 정렬된 y좌표
)

# QR 코드에 로고 붙여넣기
# 마지막 인자 logo 는 RGBA의 알파값을 mask로 사용
qr_img.paste(logo, logo_position, logo)

# 최종 QR 이미지 저장 (PNG: 투명 지원)
qr_img.save("./library/qrcode_logo.png", format="PNG")
