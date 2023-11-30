
import streamlit as st
import requests
from PIL import Image
import numpy as np
from io import BytesIO
from ML_vs_Cancer.ml_logic.read_tiff_image import read_tiff_image
import cv2

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
url = 'http://127.0.0.1:8000/predict_image'

# Placeholder for the image
image_placeholder = st.empty()

# Upload_file:
uploaded_file = st.file_uploader("Choose an image...", type=["tif", "tiff"])
if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)
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
                        st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='color:black;'> Accuracy: {pred}%</h3>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='color:black;'>Accuracy: {pred}%</h3>", unsafe_allow_html=True)
                else:
                    st.error("Error: Prediction value is None.")
            else:
                st.error("Error: 'Prediction' key not found in API response.")
        else:
            st.error(f"Error in API request. Status code: {response.status_code}")



# Upload Image
# uploaded_file = st.file_uploader("Choose an image...", type=["tif", "tiff"])
# if uploaded_file is not None:
#     try:
#         image = Image.open(uploaded_file)
#         image_placeholder.image(image, caption='Uploaded Image', use_column_width=True)

#         if st.button('Get Prediction'):
#             file_content = uploaded_file.read()
#             try:
#                 if file_content:
#                     response = requests.post(
#                         url,
#                         files={"img": ("image.tiff", file_content, "image/tiff")}
#                     )

#                     if response.status_code == 200:
#                         result = response.json()

#                         if image is not None:
#                             image_placeholder.image(image, caption='Uploaded Image', use_column_width=True)

#                         if "Prediction" in result:
#                             prediction = result["Prediction"]
#                             if prediction is not None:
#                                 if prediction < 0.5:
#                                     st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
#                                 else:
#                                     st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
#                             else:
#                                 st.error("Error: Prediction value is None.")
#                         else:
#                             st.error("Error: 'Prediction' key not found in API response.")
#                     else:
#                         st.error(f"Error in API request. Status code: {response.status_code}")
#                 else:
    #                 st.error("Error: Empty file content. Please upload a valid image.")
    #         except Exception as e:
    #             st.error(f"Error processing image: {e}")
    # except Exception as e:
    #     st.error(f"Error processing image: {e}")

# Footer
st.markdown('<p class="big-font">Thank you for using the Histopathologic Cancer Detection app!</p>', unsafe_allow_html=True)
