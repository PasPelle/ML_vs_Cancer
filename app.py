
import streamlit as st
import requests
from PIL import Image
import numpy as np
from ML_vs_Cancer.params import *

# Use HTML style tags to define custom styles
st.markdown('''
<style>
.big-font {
    font-size:20px !important;
}
</style>
''', unsafe_allow_html=True)

'''
# Histopathologic Cancer Detection
'''

# Introduction
st.markdown('<p class="big-font">Welcome to the Histopathologic Cancer Detection app. Upload a histopathologic image, and get a prediction on whether it indicates the presence of cancer.</p>', unsafe_allow_html=True)


'''
## Upload Histopathologic Image
'''

# URL of the API
url = 'https://imageanalysis-ulbdrxxy6a-ew.a.run.app/predict_image' # SERVICE_URL

# Placeholder for the image
image_placeholder = st.empty()

# Upload_file:
uploaded_file = st.file_uploader("Choose an image...", type=["tif", "tiff"])
if uploaded_file is not None:
    st.image(uploaded_file, width=300, caption="Uploaded image")
    if st.button('Get Prediction'):
        img = uploaded_file.getvalue()
        files={"file": ("image.tiff", img, "image/tiff")}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            result = response.json()
            if "Prediction" in result:
                prediction = result["Prediction"]
                if prediction is not None:
                    pred = prediction * 100
                    if prediction < 0.5:
                        pred = 100 - pred
                        st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='color:black;'>Probability: {pred:.2f}%</h3>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='color:black;'>Probability: {pred:.2f}%</h3>", unsafe_allow_html=True)
                else:
                    st.error("Error: Prediction value is None.")
            else:
                st.error("Error: 'Prediction' key not found in API response.")
        else:
            st.error(f"Error in API request. Status code: {response.status_code}")

# Footer
st.markdown('<p class="big-font">Thank you for using the Histopathologic Cancer Detection app!</p>', unsafe_allow_html=True)
