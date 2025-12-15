from concurrent.futures import ThreadPoolExecutor
from gtts import gTTS
from pathlib import Path

# from playsound import playsound
current_dir = Path(__file__).resolve().parent
poem_folder = current_dir / "poem"


# 여자 음성
def convert_to_speech(txt_file):
    with open(txt_file, "r", encoding="utf-8") as f:
        msg = f.read()
    gtts = gTTS(text=msg, lang="ko")
    save_path = current_dir / f"{txt_file.stem}.mp3"
    gtts.save(save_path)
    print(f"{txt_file.name}음성변환 완료")


with ThreadPoolExecutor() as executor:
    executor.map(convert_to_speech, poem_folder.glob("*.txt"))
