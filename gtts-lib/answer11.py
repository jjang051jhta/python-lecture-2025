from pathlib import Path
from googletrans import Translator
from gtts import gTTS
import asyncio
# current_dir = Path(__file__).resolve().parent
# 쥬피터 노트북에는 __file__이 없다/.
current_dir = Path(__file__).resolve().parent
exam_dir =  current_dir / "example"
exam01 = exam_dir / "exam01.txt"
ouput_dir = current_dir / "exam01.mp3"
async def trans():
  translator = Translator()
  with open(exam01,"r", encoding="utf-8") as f:
    msg = f.read()
    result = await translator.translate(msg,dest="ko",src="en")
    print(result)
    gtts = gTTS(text=result.text,lang="ko")
    gtts.save(ouput_dir)

# xxx.py에는 이빈트루프가 없다. 그래서 xxx.py에서 async,await를 쓴다면
# 이벤트 루프를 얹어야 한다. 아래 코드가 이벤트루프 환경을 만드는 코드이다.
asyncio.run(trans())
