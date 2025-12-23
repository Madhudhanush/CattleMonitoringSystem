import cv2
import numpy as np
import base64
import os
from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware # <--- NEW IMPORT
from ultralytics import YOLO

app = FastAPI()

# --- NEW: ALLOW EMBEDDING & EXTERNAL CALLS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows ALL websites to embed this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------------

templates = Jinja2Templates(directory="templates")

MODEL_PATH = "model.pt"
model = None

# Load Model
if os.path.exists(MODEL_PATH):
    try:
        model = YOLO(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model: {e}")
else:
    print(f"WARNING: {MODEL_PATH} not found.")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect")
async def detect_image(file: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid image file")

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(status_code=400, detail="Unable to decode image")

    results = model(img, imgsz=320)
    boxes = results[0].boxes
    count = len(boxes) if boxes else 0
    annotated_img = results[0].plot()

    success, buffer = cv2.imencode(".jpg", annotated_img)
    if not success:
        raise HTTPException(status_code=500, detail="Image encoding failed")
    
    img_base64 = base64.b64encode(buffer).decode("utf-8")

    return {
        "image": f"data:image/jpeg;base64,{img_base64}",
        "count": count
    }
