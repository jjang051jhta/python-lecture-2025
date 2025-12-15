from gtts import gTTS
from pathlib import Path

# from playsound import playsound
current_dir = Path(__file__).resolve().parent
poem_folder = current_dir / "poem"

for poem in poem_folder.glob("*.txt"):
    with open(poem, "r", encoding="utf-8") as f:
        msg = f.read()
    gtts = gTTS(text=msg, lang="ko")
    save_path = current_dir / f"{poem.stem}.mp3"
    gtts.save(save_path)
