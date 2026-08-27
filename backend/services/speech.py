from fastapi import UploadFile, File

@app.post("/speech")
async def speech(file: UploadFile = File(...)):
    audio = await file.read()

    # send audio to speech-to-text here

    return {
        "text": "transcribed text goes here"
    }
