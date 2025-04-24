# main.py (FastAPI backend)

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os 
import uuid 
from ai_style_transfer import match_cut_timing

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/process-style/")
async def process_style(referance_video: UploadFile = File(...), raw_video: UploadFile = File(...)):
    # Save uploaded videos
    ref_path = f"{UPLOAD_DIR}?{uuid.uuid4()}_refrence.mp4" 
    raw_path = f"{UPLOAD_DIR}/{uuid.uuid4()}_raw.mp4"

    with open(ref_path, "wb") as f:
        shutil.copyfileobj(reference_video.file, f)

    with open(raw_path, "wb") as f:
        shutil.copyfileobj(raw_video.file, f)    

        # Process and generate edited video
        output_path = f"{OUTPUT_DIR}/{uuid.uuid4()}_edited.mp4"
        result_path = match_cut_timing(ref_path, raw_path, output_path)

        return FileResponse(path=result_path, media_type="video/mp4", filename="edited_video.mp4")

