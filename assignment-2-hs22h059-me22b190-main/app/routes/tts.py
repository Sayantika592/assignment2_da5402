from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models.schemas import TTSRequest, TTSResponse
from app.services.tts_service import text_to_speech
import socket
import base64

router = APIRouter()

# JSON version (for tester.py + load balancing)
@router.post("/tts", response_model=TTSResponse)
def tts_json(req: TTSRequest):
    try:
        audio_path = text_to_speech(req.text)

        with open(audio_path, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode("utf-8")

        return {
            "audio_base64": audio_base64,
            "container_id": socket.gethostname()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# File version (for Swagger demo)
@router.post("/tts/file")
def tts_file(req: TTSRequest):
    try:
        audio_path = text_to_speech(req.text)
        return FileResponse(audio_path, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
