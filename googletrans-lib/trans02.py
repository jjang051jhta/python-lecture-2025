from googletrans import Translator, LANGUAGES
from pathlib import Path
import asyncio


async def trans():
    translator = Translator()
    current_dir = Path(__file__).resolve().parent
    eng_file = current_dir / "eng.txt"
    with open(eng_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line:
            result = await translator.translate(line, dest="ko", src="en")
            print(result.text)
            # ko_trans.txt에 변역본 쓰기


asyncio.run(trans())
