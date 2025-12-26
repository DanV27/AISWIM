from fastapi import FastAPI
from app.models import GenerateRequest, GenerateResponse
from app.generator import generate_workout

app = FastAPI(title="AI Swim Set Generator", version="0.1.0")

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    blocks = generate_workout(req)
    total = sum(b.yards for b in blocks)

    # default stroke if None
    stroke = req.stroke or "freestyle"

    return GenerateResponse(
        total_yards=total,
        level=req.level,
        focus=req.focus,
        stroke=stroke,
        blocks=blocks
    )
