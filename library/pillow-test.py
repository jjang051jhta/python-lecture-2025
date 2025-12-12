# pip install pillow
from PIL import Image

img = Image.open("./library/monster_big_copy.png")
# img.show()
resized_img = img.resize((64, 64))
resized_img.save("./library/logo.png")
# resized_img.show()

# img.thumbnail((200, 100))  # thumbnail은 원본 자체를 바꾼다.
# img.save("./library/monster_big_thumbnail_100.png")
# img.show()

# cropped = img.crop((50, 50, 250, 250))
# cropped = cropped.convert("RGB")
# cropped.save("./library/crop.jpg", quality=90)
# cropped.show()
