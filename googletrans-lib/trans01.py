# pip install googletrans
# pip install asyncio
from googletrans import Translator, LANGUAGES
import asyncio


async def trans():
    tanslator = Translator()
    str01 = "나는 행복합니다."
    result = await tanslator.translate(str01, dest="en", src="ko")
    print(f"{result}")
    print(f"{result.text}")
    str02 = "I am happy"
    result02 = await tanslator.translate(str02, dest="ko", src="en")
    print(f"{result02}")
    print(f"{result02.text}")


asyncio.run(trans())

print(LANGUAGES)
