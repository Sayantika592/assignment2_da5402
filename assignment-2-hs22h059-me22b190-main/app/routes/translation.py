from fastapi import APIRouter, HTTPException
from app.models.schemas import TranslationRequest, TranslationResponse
from app.services.translator_service import translate_text
import socket

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
def translate(req: TranslationRequest):
    try:
        translated = translate_text(req.text, req.target_lang)
        return {
            "translated_text": translated,
            "container_id": socket.gethostname()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
