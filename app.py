from flask import Flask, render_template, request
import tensorflow as tf
import librosa
import numpy as np
import os

app = Flask(__name__)

# Load model once
model = tf.keras.models.load_model("model/emotion_model.h5")

# Emotion labels according to your training order
EMOTIONS = ["angry", "happy", "sad", "neutral", "fear", "disgust", "surprise"]

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    return mfcc_scaled

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]
    
    if file.filename == "":
        return "No selected file"

    file_path = "uploaded.wav"
    file.save(file_path)

    # Extract features → reshape for model
    features = extract_features(file_path)
    features = np.expand_dims(features, axis=0)

    prediction = model.predict(features)
    predicted_label = EMOTIONS[np.argmax(prediction)]

    return render_template("index.html", prediction=predicted_label)

if __name__ == "__main__":
    app.run(debug=True)
