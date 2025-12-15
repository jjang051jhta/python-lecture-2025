from googletrans import Translator, LANGUAGES
from pathlib import Path
import asyncio


async def trans():
    translator = Translator()
    current_dir = Path(__file__).resolve().parent
    eng_file = current_dir / "eng.txt"
    kor_file = current_dir / "ko_trans.txt"
    with open(eng_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(kor_file, "w", encoding="utf-8") as trans_file:
        for line in lines:
            line = line.strip()
            if line:
                result = await translator.translate(line, dest="ko", src="en")

                # print(result.text)
                # ko_trans.txt에 변역본 쓰기
                trans_file.write(result.text + "\n")


asyncio.run(trans())
