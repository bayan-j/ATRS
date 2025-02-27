import cv2
import face_recognition
import numpy as np
import os


if not os.path.exists("captured_faces"):
    os.makedirs("captured_faces")

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video capture device.")
    exit()

while True:
    ret, frame = video_capture.read()
    # Convert from BGRA to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)

    if face_locations:
        cv2.imwrite("captured_faces/user_face.jpg", frame)
        print("Face Captured!")
        break


video_capture.release()
cv2.destroyAllWindows()


# Load the saved image
image = face_recognition.load_image_file("captured_faces/user_face.jpg")
# Get face encodings
face_encodings = face_recognition.face_encodings(image)[0]

if face_encodings:
    np.save("captured_faces/user_face.npy", face_encodings)
    print("Face Encoding Saved!")
else:
    print("Error: No face encodings found.")