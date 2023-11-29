import streamlit as st
import requests
from PIL import Image
import io

# Histopathologic Cancer Detection

# Introduction
st.markdown('''
Welcome to the Histopathologic Cancer Detection app. Upload a histopathologic slide image, and get a prediction on whether the slide indicates the presence of cancer.
''')

'''
## Upload Histopathologic Slide Image
'''

# Placeholder for the image
image_placeholder = st.empty()

# Upload Image
uploaded_file = st.file_uploader("Choose a slide image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_placeholder.image(image, caption='Uploaded Image', use_column_width=True)

'''
## Cancer Detection Prediction
'''

# URL of the API
url = 'YOUR_API_URL'

# Button to make the prediction
if st.button('Get Prediction') and uploaded_file is not None:
    # Convert the image to bytes for API request
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_byte = buffered.getvalue()

    # Send a request to the API
    response = requests.post(url, files={"file": img_byte})

    # Check if the request was successful
    if response.status_code == 200:
        prediction, accuracy = response.json()["prediction"], response.json()["accuracy"]
        if prediction == 1:
            st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
        st.write(f"Prediction Accuracy: {accuracy}%")
    else:
        st.error("Error in API request")

# Footer
st.markdown('''
Thank you for using the Histopathologic Cancer Detection app!
''')
