from flask import Flask, render_template, request, redirect, url_for, session
import tensorflow as tf
import librosa
import numpy as np
import os

app = Flask(__name__)
app.secret_key = "misha_secret_key"


model = tf.keras.models.load_model("model/emotion_model.keras")

EMOTIONS = ["angry", "happy", "sad", "neutral", "fear", "disgust", "surprise"]


users = {}

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

#ROUTES 

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users[email] = password
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email] == password:
            session["user"] = email
            return redirect(url_for("emotion"))
        else:
            return "Invalid email or password"

    return render_template("login.html")

@app.route("/emotion", methods=["GET", "POST"])
def emotion():
    if "user" not in session:
        return redirect(url_for("login"))

    prediction = None

    if request.method == "POST":
        file = request.files["file"]
        file_path = "uploads/audio.wav"
        file.save(file_path)

        features = extract_features(file_path)
        features = np.expand_dims(features, axis=0)

        result = model.predict(features)
        prediction = EMOTIONS[np.argmax(result)]

        os.remove(file_path)

    return render_template("index.html", prediction=prediction)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------- RUN ----------

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
