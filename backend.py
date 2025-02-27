
from flask import Flask, request, render_template, jsonify
import face_recognition
import numpy as np


app = Flask(__name__)

# Load registered user encoding (Assuming user1 is pre-registered)
stored_encoding = np.load("captured_faces/user_face.npy")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    file = request.files['image']
    image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) > 0:
        matches = face_recognition.compare_faces([stored_encoding], face_encodings[0])
        if matches[0]:
            return jsonify({"message": "✅ Login Successful!"})
    
    return jsonify({"message": "❌ Unauthorized"}), 401