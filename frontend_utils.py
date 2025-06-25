# File: frontend_utils.py

import streamlit as st

def style_page():
    st.set_page_config(page_title="Age Verification", layout="centered")

    st.markdown("""
        <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)
