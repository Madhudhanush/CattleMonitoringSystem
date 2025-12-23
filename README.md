# 🐄 Cattle Monitoring System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-purple)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)

A real-time AI-powered system designed to detect and count cattle using Computer Vision. This project was developed to assist farmers in automating livestock monitoring using simple webcams or image uploads.

## 🚀 Live Demo

Experience the application live on Hugging Face Spaces:
**[👉 Click Here to View Live Demo](https://madhudhanushk-cattlemonitoringsystem.hf.space)**

*(Note: The live demo is hosted on a CPU-basic instance, so detection speed may vary.)*

---

## ✨ Key Features

* **📸 Live Webcam Detection:** Real-time object detection directly from the browser using the device camera.
* **📁 Image Upload Analysis:** Upload static images to detect and count cattle instantly.
* **🔢 Automated Counting:** Displays the total count of detected cattle in the current frame.
* **📱 Responsive Design:** Fully functional on both Desktop and Mobile devices.
* **🔒 Secure Backend:** Built with FastAPI and validated using Pydantic.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **AI/ML:** Ultralytics YOLOv8, OpenCV (Headless)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Jinja2 Templates
* **Deployment:** Docker, Hugging Face Spaces

---

## 📂 Project Structure

```text
CattleMonitoringSystem/
├── templates/
│   └── index.html       # Frontend UI with camera logic
├── Dockerfile           # Configuration for containerization
├── main.py              # FastAPI application entry point
├── model.pt             # Custom trained YOLOv8 weights
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
