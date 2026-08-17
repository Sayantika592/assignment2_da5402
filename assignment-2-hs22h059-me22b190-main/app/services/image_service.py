import requests

import uuid

API_KEY = os.getenv("STABILITY_API_KEY")
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/*",
}

def generate_image(prompt: str):
    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png"),
    }

    response = requests.post(API_URL, headers=headers, files=files)

    if response.status_code != 200:
        raise Exception(f"Stability API error: {response.text}")

    image_path = f"generated_{uuid.uuid4()}.png"

    with open(image_path, "wb") as f:
        f.write(response.content)

    return image_path
