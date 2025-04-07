import streamlit as st
import cv2
import numpy as np
from PIL import Image

def ndvi(image):
    img = np.array(image.convert('RGB'))
    red = img[:, :, 0].astype(float)
    nir = img[:, :, 2].astype(float)
    ndvi = (nir - red) / (nir + red)
    return ndvi

def show():
    st.title("Upload Image for NDVI Classification")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        ndvi_result = ndvi(image)
        st.image(ndvi_result, caption="NDVI Output", use_column_width=True)