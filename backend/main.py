import os
from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel
from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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

    # Convert speech to text
    segments, info = model.transcribe("/tmp/audio.webm")

    text = ""

    for segment in segments:
        text += segment.text

    # Send the text to Gemini
    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=text
    )

    # Return both results
    return {
        "transcription": text.strip(),
        "response": response.text
    }
