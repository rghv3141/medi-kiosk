from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel

app = FastAPI()

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


@app.get("/")
def home():
    return {"message": "Backend is working"}


@app.post("/speech")
async def speech(file: UploadFile = File(...)):

    audio = await file.read()

    with open("/tmp/audio.webm", "wb") as f:
        f.write(audio)

    segments, info = model.transcribe("/tmp/audio.webm")

    text = ""

    for segment in segments:
        text += segment.text

    return {
        "text": text.strip()
    }
