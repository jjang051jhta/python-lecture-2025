from pathlib import Path
from googletrans import Translator
from gtts import gTTS
import asyncio
from playsound import playsound

current_dir = Path(__file__).resolve().parent
eng_path = current_dir / "eng02.txt"
kor_path = current_dir / "kor02.txt"
mp3_path = current_dir / "kor02_trans.mp3"

kor_lines = []


# 번역
async def trans():
    translator = Translator()
    with open(eng_path, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 각줄을 읽어서 list만들기

    for line in lines:
        line = line.strip()
        if not line:
            kor_lines.append("")
            continue
        result = await translator.translate(line, src="en", dest="ko")
        kor_lines.append(result.text)


asyncio.run(trans())
with open(kor_path, "w", encoding="utf-8") as f02:
    for line in kor_lines:
        f02.write(line + "\n")
# print(kor_lines)
with open(kor_path, "r", encoding="utf-8") as f03:
    msg = f03.read()
gtts = gTTS(text=msg, lang="ko")
gtts.save(mp3_path)
playsound(str(mp3_path))
