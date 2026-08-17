

# Multi-Modal AI API — Assignment 2

## Overview

This project implements a **multi-modal AI microservice** exposing multiple capabilities through REST APIs using **FastAPI**. The system integrates multiple AI modalities into a unified service and demonstrates the complete lifecycle from development to distributed deployment using **Docker Swarm orchestration**.

The service supports:

* Text Translation
* Image Generation
* Named Entity Recognition (NER)
* Text-to-Speech (TTS)

The application follows a modular architecture separating **routes**, **services**, and **schemas**, and uses collaborative Git workflows with feature branches and pull requests.



## Team

* **Sayantika** — Translation, Image Generation
* **Anubhav** — Named Entity Recognition (NER), Text-to-Speech (TTS)



## System Architecture

The application is structured using layered separation of concerns:

```
Client Request
      ↓
Docker Swarm Ingress Network
      ↓
Load Balancer (Routing Mesh)
      ↓
FastAPI Container Replica
      ↓
Service Layer (AI Modules)
      ↓
Response with Container ID
```

Each API response includes a **container identifier** using `socket.gethostname()` to track which replica handled the request during load balancing experiments.

---

## Project Structure

```
assignment-2/
│
├── app/
│   ├── main.py                     # FastAPI application entry point
│   │
│   ├── routes/                     # API route definitions
│   │   ├── image_gen.py
│   │   ├── ner.py
│   │   ├── translation.py
│   │   └── tts.py
│   │
│   ├── services/                   # Business logic layer
│   │   ├── image_service.py
│   │   ├── ner_service.py
│   │   ├── translator_service.py
│   │   └── tts_service.py
│   │
│   ├── models/                     # Pydantic schemas
│   │   └── schemas.py
│   │
│   └── __init__.py
│
├── audio/                          # Generated speech files
│
├── Dockerfile                      # Container build configuration
├── docker-stack.yml                # Docker Swarm deployment config
├── requirements.txt                # Python dependencies
├── tester.py                       # Load balancing test script
├── CONFLICT.md                     # Merge conflict documentation
├── README.md
└── .dockerignore / .gitignore
```


## Local Installation

### 1. Clone repository

```bash
git clone https://github.com/DA5402-MLOps-JAN26/assignment-2-hs22h059-me22b190.git
cd assignment-2-hs22h059-me22b190
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install spaCy model

```bash
python -m spacy download en_core_web_sm
```

### 5. Environment variables

```bash
export STABILITY_API_KEY='your_key_here'
```

---

## Running Locally

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8001
```

Interactive docs:

```
http://127.0.0.1:8001/docs
```

---

## API Endpoints

### Translation

```
POST /translate
```

```json
{
  "text": "Hello world",
  "target_lang": "fr"
}
```

---

### Image Generation

```
POST /generate-image
```

```json
{
  "prompt": "A futuristic city at sunset"
}
```

---

### Named Entity Recognition (NER)

```
POST /ner
```

```json
{
  "text": "Elon Musk founded SpaceX in California."
}
```

---

### Text-to-Speech (TTS)

```
POST /tts
```

```json
{
  "text": "Hello, this is a speech synthesis test."
}
```

Returns an MP3 file.

---

# Dockerization

The application is containerized using a lightweight Python base image.

Key features:

* Python 3.11 slim image
* Dependencies installed via requirements file
* Environment variables for API keys
* Container metadata returned in API responses
* Optimized Docker layer caching for faster rebuilds

Build image:

```bash
docker build -t multimodal-api .
```

Run container:

```bash
docker run -p 8001:8000 multimodal-api
```


# Docker Swarm Deployment

The system was deployed on a Docker Swarm cluster with:

* **Manager Node:** HP Victus machine
* **Worker Node:** Docker Desktop environment

### Initialize Swarm (Manager)

```bash
docker swarm init
```

### Join Worker Node

```bash
docker swarm join --token <token> <manager-ip>:2377
```

### Deploy Stack

```bash
docker stack deploy -c docker-stack.yml multimodal
```

The service is deployed with **4 replicas**, enabling distributed request handling.


## Overlay Network Explanation

Docker Swarm automatically creates an **overlay network**, which allows containers across different machines to communicate securely as if they were on the same local network. This eliminates the need for manual network configuration in distributed environments.



## Load Balancing

Docker Swarm uses an **ingress routing mesh** to expose a single service endpoint while distributing incoming traffic across multiple replicas using round-robin scheduling.

Each API response returns:

```
container_id
```

which confirms which replica handled the request.

---

# Load Testing

A concurrent client script (`tester.py`) sends 100 requests to verify load balancing. We have sent 200 requests to 2 features.

Example usage:

```bash
python tester.py
```

The output displays request distribution across container IDs, demonstrating successful load balancing.


# Git Workflow

Each feature was developed in its own branch:

```
feature/translation
feature/image-generation
feature/ner
feature/tts
```

Pull requests were reviewed before merging into `main`.

A merge conflict was intentionally triggered and resolved to demonstrate collaborative development practices. Details are documented in `CONFLICT.md`.

---

# Dependencies

Key libraries:

* FastAPI
* Uvicorn
* spaCy
* gTTS
* deep-translator
* requests
* python-dotenv

---

# Testing

Endpoints were tested using:

* FastAPI Swagger UI
* Local execution via uvicorn
* Docker container execution
* Distributed cluster deployment
* Concurrent load testing

---

# Notes

* Generated media files are stored locally during runtime.
* API keys are loaded via environment variables for security.
* The system demonstrates scalable AI deployment using container orchestration.

---

# AI Disclosure Appendix

AI assistance was used to support debugging, Docker configuration guidance, and documentation drafting. All implementation logic was reviewed, validated, and executed by the authors. The final system reflects the authors’ understanding, with AI serving only as a supplementary aid.



# License

This project is for academic purposes only.


