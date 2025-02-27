from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import face_recognition
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = 'captured_faces'
app.config['VERIFIED_FOLDER'] = 'verified_faces'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the 'captured_faces' and 'verified_faces' folders exist
for folder in [app.config['UPLOAD_FOLDER'], app.config['VERIFIED_FOLDER']]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Index route (for displaying the upload form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if there is an image file in the request
    if 'image' not in request.files:
        return 'No file part', 400
    
    file = request.files['image']
    
    # If no file was selected by the user
    if file.filename == '':
        return 'No selected file', 400
    
    # If the file is allowed and valid
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Sanitize filename to prevent security issues
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save file to the upload folder
        return f"Image uploaded and saved as {filename}", 200
    else:
        return "Invalid file type. Please upload a valid image.", 400

# Route for verification (example for facial recognition or similar)
@app.route('/verify', methods=['POST'])
def verify_image():
    print("Verification route hit")
    # Check if the image is in the request
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    
    if file.filename == '':
        return 'No selected file', 400
    
    # Here you would add your verification logic
    # For now, let's just check if the file is allowed and return a success message
    if file and allowed_file(file.filename):
        # You could compare this image to another known image, e.g., by using facial recognition, etc.
        # For now, we will just save it to the "verified_faces" folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['VERIFIED_FOLDER'], filename))
        return f"Image uploaded for verification and saved as {filename}", 200
    else:
        return "Invalid file type. Please upload a valid image.", 400

# Running the app
if __name__ == 'main':
    app.run(debug=True)