import os

# pip install google.cloud
from google.cloud import texttospeech
from playsound import playsound
from pathlib import Path


current_dir = Path(__file__).resolve().parent


def gtts_advanced(
    path=current_dir / "seosi.txt",
    output_file=current_dir / "seosi_advanced.mp3",
    language_code="ko-KR",
    voice_name="ko-KR-Neural2-B",
    speaking_rate=1.05,
):
    client = texttospeech.TextToSpeechClient()
    with open(path, "r", encoding="utf-8") as f:
        msg = f.read()
    synthesis_input = texttospeech.SynthesisInput(text=msg)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate,
        pitch=0.0,
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open(output_file, "wb") as output:
        output.write(response.audio_content)
        print(f"seosi 음성파일 생성완료 : {output_file}")
    playsound(str(current_dir / output_file))


gtts_advanced()
