import streamlit as st
import cv2

def show():
    st.title("Live Webcam Capture")

    camera = cv2.VideoCapture(0)
    if st.button("Capture Image"):
        ret, frame = camera.read()
        if ret:
            st.image(frame, caption="Captured Image")
            cv2.imwrite("captured.jpg", frame)