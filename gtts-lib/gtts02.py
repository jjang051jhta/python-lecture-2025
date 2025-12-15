# google text to speech
# pip install gTTS
# pip install playsound
from gtts import gTTS
from pathlib import Path
from playsound import playsound

current_dir = Path(__file__).resolve().parent
file_path = current_dir / "seosi.txt"
with open(file_path, "r", encoding="utf-8") as f:
    msg = f.read()
gtts = gTTS(text=msg, lang="ko")
save_path = current_dir / "seosi.mp3"
gtts.save(save_path)
playsound(str(save_path))
