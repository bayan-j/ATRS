import cv2
import face_recognition as fr
import json
import os

photo_capture = cv2.VideoCapture(0)
image = fr.load_image_file("photos.jpg")

Face_data_file = "face_encodings.json"

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect faces in the frame
face_locations = face_recognition.face_locations(rgb_img)
face_encodings = face_recognition.face_encodings(rgb_img, face_locations)


cap.release()
cv2.destroyAllWindows()
