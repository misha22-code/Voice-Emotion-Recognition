🎙️ Voice Emotion Recognition Web App

A Flask-based Machine Learning web application that detects human emotions from voice recordings using a trained deep learning model.
This project is designed as a final year project and demonstrates the integration of AI, ML, and Web Technologies.

📌 Project Overview

Voice Emotion Recognition helps analyze human emotions from speech signals.
This system allows users to:

Sign up and log in

Upload or record voice samples

Predict emotions such as Happy, Sad, Angry, Neutral, etc.

View results on a clean and user-friendly interface

🧠 Technologies Used
🔹 Backend

Python

Flask

🔹 Machine Learning

TensorFlow / Keras

Pre-trained emotion recognition model (.keras)

🔹 Frontend

HTML5

CSS3

🔹 Others

NumPy

Librosa (for audio processing)

📂 Folder Structure
Voice-Emotion-Recognition/
│
├── model/
│   └── emotion_model.keras
│
├── static/
│   └── style.css
│
├── templates/
│   ├── landing.html
│   ├── login.html
│   ├── signup.html
│   └── index.html
│
├── uploads/
│
├── app.py
├── requirements.txt
└── README.md

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/voice-emotion-recognition.git
cd voice-emotion-recognition

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask App
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

🔐 Authentication System

User Sign Up

User Login

Protected emotion recognition page

Clean separation of landing, auth, and main app pages

🎨 UI Design

Landing page with attractive color theme

Authentication pages (Login / Signup) with minimal design

Main emotion detection page uses a different color theme for clarity

Fully responsive and easy to understand

🎯 Features

🎤 Voice upload support

🧠 AI-based emotion prediction

🔐 Authentication system

🗂 Organized Flask structure

📊 Accurate ML model

🧪 Suitable for academic evaluation

📚 Use Cases

Academic projects

Emotion analysis research

AI & ML learning

Human–computer interaction systems

🏫 Final Year Project Note

This project fulfills Final Year Project (FYP) requirements by demonstrating:

Machine Learning implementation

Web-based system design

Practical AI application

Clean architecture and documentation

👩‍💻 Author

Misha Noor
BS Computer Science
Final Year Project

📄 License

This project is for educational purposes only.