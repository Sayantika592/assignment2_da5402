import requests
from collections import Counter
import concurrent.futures
import random

LEADER_IP = "127.0.0.1"
PORT = "8001"

NER_URL = f"http://{LEADER_IP}:{PORT}/ner"
TRANSLATE_URL = f"http://{LEADER_IP}:{PORT}/translate"

def call_api(_):
    try:
        if random.random() < 0.5:
            r = requests.post(
                NER_URL,
                json={"text": "Apple is hiring in London."},
                timeout=5
            )
        else:
            r = requests.post(
                TRANSLATE_URL,
                json={"text": "Hello world", "target_lang": "fr"},
                timeout=5
            )

        return r.json().get("container_id")

    except Exception:
        return "Failed"

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(call_api, range(200)))
print(Counter(results))