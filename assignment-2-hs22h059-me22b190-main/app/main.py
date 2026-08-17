from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import translation, image_gen, ner, tts
import socket

load_dotenv()

app = FastAPI(title="Multi-Modal AI API")

app.include_router(translation.router)
app.include_router(image_gen.router)
app.include_router(ner.router)
app.include_router(tts.router)

@app.get("/id")
def get_container_id():
    return {"container_id" = socket.gethostname()}
