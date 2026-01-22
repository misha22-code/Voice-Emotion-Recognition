from flask import Flask, render_template, request
import tensorflow as tf
import librosa
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained emotion recognition model (loaded once)
model = tf.keras.models.load_model("model/emotion_model.h5")

# Emotion labels (same order as model training)
EMOTIONS = ["angry", "happy", "sad", "neutral", "fear", "disgust", "surprise"]


def extract_features(file_path):
    """
    Extract MFCC features from an audio file
    """
    audio, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    return mfcc_scaled


@app.route("/")
def index():
    """
    Render home page
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Handle audio upload and emotion prediction
    """
    if "file" not in request.files:
        return render_template("index.html", prediction="No file uploaded")

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html", prediction="No file selected")

    # Save uploaded file
    file_path = "uploaded.wav"
    file.save(file_path)

    try:
        # Feature extraction
        features = extract_features(file_path)
        features = np.expand_dims(features, axis=0)

        # Model prediction
        prediction = model.predict(features)
        predicted_label = EMOTIONS[np.argmax(prediction)]

    except Exception as e:
        predicted_label = "Error processing audio"

    finally:
        # Remove uploaded file after prediction
        if os.path.exists(file_path):
            os.remove(file_path)

    return render_template("index.html", prediction=predicted_label)


if __name__ == "__main__":
    app.run(debug=True)
