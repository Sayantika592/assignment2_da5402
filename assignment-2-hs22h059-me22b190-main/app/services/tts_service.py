from gtts import gTTS
import uuid
import os

def text_to_speech(text: str):
    os.makedirs("audio", exist_ok=True)
    filename = f"audio/speech_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    return filename
