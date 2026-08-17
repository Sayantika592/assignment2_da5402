from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models.schemas import ImageRequest, ImageResponse
from app.services.image_service import generate_image
import socket
import base64

router = APIRouter()

# JSON version (for tester.py + load balancing)
@router.post("/generate-image", response_model=ImageResponse)
def generate_json(req: ImageRequest):
    try:
        image_path = generate_image(req.prompt)

        with open(image_path, "rb") as f:
            image_base64 = base64.b64encode(f.read()).decode("utf-8")

        return {
            "image_base64": image_base64,
            "container_id" = socket.gethostname()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-image/file")
def generate_file(req: ImageRequest):
    try:
        image_path = generate_image(req.prompt)
        return FileResponse(image_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
