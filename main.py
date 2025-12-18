import cv2
import numpy as np
import base64
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load YOLOv8 Nano for high speed
model = YOLO("model.pt") 

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/detect")
async def detect_image(file: UploadFile = File(...)):
    # 1. Read uploaded image (works for both Snap and Upload)
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 2. Run Inference (imgsz=320 for speed)
    results = model(img, imgsz=320)
    
    # 3. Process Result
    count = len(results[0].boxes)
    res_plotted = results[0].plot()
    
    # 4. Convert to Base64 to send to UI
    _, buffer = cv2.imencode('.jpg', res_plotted)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return {
        "image": f"data:image/jpeg;base64,{img_base64}", 
        "count": count
    }

if __name__ == "__main__":
    import uvicorn
    import os
    # Get port from environment (Render/Heroku set this automatically)
    port = int(os.environ.get("PORT", 8000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)