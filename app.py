import streamlit as st
import requests
from PIL import Image
import io

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

# Placeholder for the image
image_placeholder = st.empty()

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["tif", "tiff"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_placeholder.image(image, caption='Uploaded Image', use_column_width=True)

'''
## Cancer Detection Prediction
'''

# URL of the API
url = 'YOUR_API_URL'

# # Button to make the prediction
# if st.button('Get Prediction') and uploaded_file is not None:
#     # Convert the image to bytes for API request
#     buffered = io.BytesIO()
#     image.save(buffered, format="JPEG")
#     img_byte = buffered.getvalue()

#     # Send a request to the API
#     response = requests.post(url, files={"file": img_byte})

#     # Check if the request was successful
#     if response.status_code == 200:
#         prediction, accuracy = response.json()["prediction"], response.json()["accuracy"]
#         if prediction == 1:
#             st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
#         st.write(f"Prediction Accuracy: {accuracy}%")
#     else:
#         st.error("Error in API request")

# Button to make the prediction - TEST!
if st.button('Get Prediction') and uploaded_file is not None:
    # Use the length of the file name to generate a pseudo-random number
    def get_pseudo_random_prediction(file_name):
        return len(file_name) % 2  # Returns 0 or 1

    # Get the pseudo-random prediction
    prediction = get_pseudo_random_prediction(uploaded_file.name)
    accuracy = len(uploaded_file.name) % 30 + 70  # Random accuracy between 70% and 99%

    # Display the prediction result
    if prediction == 1:
        st.markdown(f"<h2 style='color:red;'>Malignant</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='color:green;'>Non-Malignant</h2>", unsafe_allow_html=True)
    st.write(f"<p class='big-font'>Prediction Accuracy: {accuracy}%</p>", unsafe_allow_html=True)


# Footer
st.markdown('<p class="big-font">Thank you for using the Histopathologic Cancer Detection app!</p>', unsafe_allow_html=True)
