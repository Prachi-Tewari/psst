# File: app.py

import streamlit as st
from ocr_utils import extract_dob_and_age
from face_utils import get_face_match_score
from frontend_utils import style_page
import tempfile
import cv2
import numpy as np
import os
import base64

style_page()  # Apply styling

st.title("Age & Identity Verification System")
st.markdown("Upload your Aadhar card and capture a live selfie to verify your identity.")

id_image_file = st.file_uploader("Upload Aadhar Card Image", type=["jpg", "jpeg", "png"])

# 📸 Capture selfie directly from webcam
st.markdown("### Capture Live Selfie")
selfie_bytes = st.camera_input("Take a selfie")

if st.button("Verify"):
    if id_image_file and selfie_bytes:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as id_temp:
            id_temp.write(id_image_file.read())
            id_img_path = id_temp.name

        # Save the live selfie to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as selfie_temp:
            selfie_temp.write(selfie_bytes.getvalue())
            selfie_img_path = selfie_temp.name

        id_image = cv2.imread(id_img_path)
        selfie_image = cv2.imread(selfie_img_path)

        dob, age, is_adult = extract_dob_and_age(id_image)
        if dob is None:
            st.error("Could not extract Date of Birth from Aadhar image.")
            st.stop()

        match_score = get_face_match_score(id_img_path, selfie_img_path)

        st.success("Verification Complete")
        st.markdown(f"**Date of Birth:** {dob}")
        st.markdown(f"**Age:** {age}")
        st.markdown(f"**18+ Status:** {'Yes' if is_adult else 'No'}")
        st.markdown(f"**Face Match Score:** {match_score}%")

        if is_adult and match_score >= 70:
            st.markdown("\n\n✅ **Verification Passed**")
        else:
            st.markdown("\n\n❌ **Verification Failed**")

    else:
        st.warning("Please upload the Aadhar card and capture a selfie.")