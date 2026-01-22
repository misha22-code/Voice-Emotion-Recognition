# 🎤 Voice Emotion Recognition (Forked & Extended)

A Python-based web application that detects human emotions from voice audio using **TensorFlow** and **Flask**.  
Users can upload a `.wav` audio file, listen to it, and receive real-time emotion predictions.

> 🔖 This project is **forked from the original work by Hamama Komal**.  
> I am maintaining and extending this repository for **learning, experimentation, and future enhancements** in AI & Machine Learning.

---

## 👩‍💻 Maintained by
**Misha Noor**  
Mobile Application Developer transitioning into **AI & Machine Learning**  
Interested in **Chatbots, AI Agents, and Intelligent Systems**

---

## 🚀 My Learning Goals & Modifications
- Understanding end-to-end ML project structure
- Learning how to integrate **TensorFlow models with Flask**
- Exploring **audio feature extraction (MFCCs)**
- Improving documentation and UI
- Planning future enhancements (chatbot & AI agent integration)

---

## ✨ Features
- 🎯 Predict emotions: **Angry, Happy, Sad, Neutral, Fear, Disgust, Surprise**
- 📂 Upload `.wav` audio files via web interface
- ▶️ Play audio before prediction
- ⚡ Real-time emotion prediction using TensorFlow
- 🎨 Modern UI with gradient background and animations
- ☁️ Deployable on free platforms (Render, HuggingFace Spaces)

---

## 🗂 Project Structure

```text
Voice-Emotion-Recognition/
│── app.py                 # Flask backend
│── model/
│     └── emotion_model.keras   # Trained TensorFlow model
│── templates/
│     └── index.html        # Frontend HTML
│── static/                # CSS / assets (optional)
│── requirements.txt       # Python dependencies
```
⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/misha22-code/Voice-Emotion-Recognition.git
cd Voice-Emotion-Recognition

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the App Locally
python app.py


Open in browser:

http://127.0.0.1:5000/


Upload a .wav file and view the predicted emotion 

🧠 How It Works

Audio Upload – User uploads .wav file

Feature Extraction – MFCC features extracted using librosa

Prediction – TensorFlow model predicts emotion

Display – Emotion shown on UI with animation

🛠 Technologies Used

Python

Flask

TensorFlow

Librosa

NumPy

SoundFile

HTML / CSS

Gunicorn (deployment)

☁️ Deployment

You can deploy this project on:

Render

HuggingFace Spaces

Just push the repository and configure a Python + Flask runtime.

📜 License

This project is open-source and free to use for learning and educational purposes.

🌱 Final Note

This project is part of my journey into AI, Machine Learning, Chatbots, and Intelligent Systems.
More improvements and experiments will be added as I grow my skills 🚀


