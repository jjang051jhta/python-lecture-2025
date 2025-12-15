# google text to speech
# pip install gTTS
# pip install playsound
from gtts import gTTS
from pathlib import Path
from playsound import playsound

current_dir = Path(__file__).resolve().parent

msg = "gtts는 구글 텍스트 투 스피치입니다. 텍스트를 음성으로 바꿔줍니다."
gtts = gTTS(text=msg, lang="ko")
save_path = current_dir / "msg.mp3"
gtts.save(save_path)
playsound(str(save_path))
