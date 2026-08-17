from fastapi import APIRouter, HTTPException
from app.models.schemas import NERRequest, NERResponse
from app.services.ner_service import extract_entities
import socket

router = APIRouter()

@router.post("/ner", response_model=NERResponse, summary='NER')
def ner(req: NERRequest):
    try:
        entities = extract_entities(req.text)
        return {
            "entities": entities,
            "container_id" = socket.gethostname()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
