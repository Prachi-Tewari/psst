# File: face_utils.py

import face_recognition
import numpy as np

# No API key needed unless you're replacing this with AWS/Azure. This uses face_recognition (local).

def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, known_face_locations=locations)
    if encodings:
        return encodings[0]
    return None

def get_face_match_score(id_img_path, selfie_img_path):
    id_encoding = get_face_encoding(id_img_path)
    selfie_encoding = get_face_encoding(selfie_img_path)

    if id_encoding is None or selfie_encoding is None:
        return 0.0

    distance = np.linalg.norm(id_encoding - selfie_encoding)
    score = max(0, 1 - distance) * 100  # convert to percentage
    return round(score, 2)
