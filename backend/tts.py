from gtts import gTTS
import os
import uuid

def generate_audio(text, language):
    filename = f"audio_{uuid.uuid4()}.mp3"
    path = os.path.join("uploads", filename)

    lang_code = "hi" if language == "hindi" else "en"

    tts = gTTS(text=text, lang=lang_code)
    tts.save(path)

    return path
