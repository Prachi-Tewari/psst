# face_utils.py using InsightFace (Mac compatible)

from insightface.app import FaceAnalysis
import numpy as np
import cv2

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0)

def get_face_embedding(img_path):
    img = cv2.imread(img_path)
    faces = app.get(img)
    if not faces:
        return None
    return faces[0].embedding

def get_face_match_score(id_img_path, selfie_img_path):
    emb1 = get_face_embedding(id_img_path)
    emb2 = get_face_embedding(selfie_img_path)
    if emb1 is None or emb2 is None:
        return 0.0
    cosine_similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    return round(cosine_similarity * 100, 2)
