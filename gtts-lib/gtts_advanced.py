import os
from pathlib import Path

# Google Cloud Text-to-Speech 라이브러리
# pip install google-cloud-texttospeech
from google.cloud import texttospeech

# 생성된 mp3 파일을 바로 재생하기 위한 라이브러리
# pip install playsound
from playsound import playsound


# ==================================================
# 1 Google Cloud 인증 (서비스 계정 키)
# ==================================================
# Google Cloud 라이브러리는 이 환경변수를 통해
# "어떤 계정으로 API를 쓰는지"를 확인함
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    r"D:\jjang051-lecture\python-lecture\xxx.json"
)

# 환경변수 정상 설정 확인 (None이면 인증 못 찾는 상태)
print("ADC =", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))


# ==================================================
# 2 현재 작업 중인 폴더 (스크립트 위치 기준)
# ==================================================
current_dir = Path(__file__).resolve().parent


# ==================================================
# 3 Google Cloud TTS 함수
# ==================================================
def gtts_advanced(
    path=current_dir / "seosi.txt",  # 읽을 텍스트 파일
    output_file=current_dir / "seosi_advanced.mp3",  # 저장할 mp3 파일
    language_code="ko-KR",  # 언어 코드 (한국어)
    voice_name="ko-KR-Neural2-B",  # 고품질 Neural2 음성
    speaking_rate=1.05,  # 말하기 속도 (0.25 ~ 4.0)
):
    """
    텍스트 파일을 읽어서
    Google Cloud Text-to-Speech로 음성(mp3)을 생성하고
    바로 재생하는 함수
    """

    # ----------------------------------------------
    # 1) TTS 클라이언트 생성
    # ----------------------------------------------
    # 이 시점에서 GOOGLE_APPLICATION_CREDENTIALS 환경변수를 사용해 인증
    client = texttospeech.TextToSpeechClient()

    # ----------------------------------------------
    # 2) 텍스트 파일 읽기
    # ----------------------------------------------
    msg = Path(path).read_text(encoding="utf-8").strip()

    # 텍스트가 비어 있으면 중단
    if not msg:
        print("텍스트 파일이 비어 있습니다.")
        return

    # ----------------------------------------------
    # 3) 합성할 텍스트 객체 생성
    # ----------------------------------------------
    synthesis_input = texttospeech.SynthesisInput(text=msg)  # 실제 읽을 텍스트

    # ----------------------------------------------
    # 4) 음성(목소리) 설정
    # ----------------------------------------------
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,  # 언어 / 지역 (ko-KR)
        name=voice_name,  # 실제 목소리 선택
        # 성별 힌트 (name 지정 시 거의 참고용)
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        # 선택값:
        # FEMALE  / MALE / NEUTRAL
    )

    # ----------------------------------------------
    # 5) 오디오 출력 옵션 (수치 조절 핵심!)
    # ----------------------------------------------
    audio_config = texttospeech.AudioConfig(
        # 출력 오디오 포맷
        audio_encoding=texttospeech.AudioEncoding.MP3,
        # 선택값:
        # MP3 / LINEAR16(wav) / OGG_OPUS
        # 말하기 속도
        # 기본값: 1.0
        # 범위: 0.25 ~ 4.0
        speaking_rate=speaking_rate,
        # 음높이 (톤)
        # 기본값: 0.0
        # 범위: -20.0 ~ +20.0
        # 음수 → 낮고 차분 / 양수 → 밝고 높음
        pitch=0.0,
        # 볼륨 증폭 (선택)
        # 기본값: 0.0
        # 범위: -96.0 ~ +16.0
        volume_gain_db=2.0,
        # 샘플링 레이트 (선택, 보통 생략 가능)
        # sample_rate_hertz=24000
    )

    # ----------------------------------------------
    # 6) 음성 합성 요청 (Google 서버 호출)
    # ----------------------------------------------
    response = client.synthesize_speech(
        input=synthesis_input,  # 읽을 텍스트
        voice=voice,  # 음성 설정
        audio_config=audio_config,
    )

    # ----------------------------------------------
    # 7) mp3 파일로 저장
    # ----------------------------------------------
    # response.audio_content 는 bytes(바이너리 데이터)
    Path(output_file).write_bytes(response.audio_content)
    print(f"seosi 음성파일 생성완료 : {output_file}")

    # ----------------------------------------------
    # 8) 생성된 음성 파일 재생
    # ----------------------------------------------
    playsound(str(output_file))


# ==================================================
# 4 함수 실행
# ==================================================
gtts_advanced()
