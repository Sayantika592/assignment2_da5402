from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

class TranslationResponse(BaseModel):
    translated_text: str
    container_id: str

class ImageRequest(BaseModel):
    prompt: str

class ImageResponse(BaseModel):
    image_base64: str
    container_id: str

class NERRequest(BaseModel):
    text: str

class NERResponse(BaseModel):
    entities: list
    container_id: str

class TTSRequest(BaseModel):
    text: str

class TTSResponse(BaseModel):
    audio_base64: str
    container_id: str