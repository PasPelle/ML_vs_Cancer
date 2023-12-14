# TEAM

**Daniel Stark**: Background in 3D design … please write 1-3 sentences for yourself.<br>
<a href="https://www.linkedin.com/in/dstark2022/" target="blank"><img align="center" src="./linked-in-alt.svg" alt="kristjanqarri" height="20" width="27" /></a> <a href="https://github.com/drostark" target="blank"><img align="center" src="./octocat.svg" alt="kristjanqarri" height="20" width="27" /></a><br>
**Katažyna Balcevič**: Experienced Android developer with a strong four-year background in the field, passionate about integrating expertise in ML Engineering with a dedication to transforming the healthcare industry.<br>
<a href="https://www.linkedin.com/in/katazynabalcevic/" target="blank"><img align="center" src="./linked-in-alt.svg" alt="kristjanqarri" height="20" width="27" /></a> <a href="https://github.com/Katazynab" target="blank"><img align="center" src="./octocat.svg" alt="kristjanqarri" height="20" width="27" /></a><br>
**Kristjan Qarri**: Medical Technology Engineer & passionate about the application of technology in healthcare.<br>
<a href="https://linkedin.com/in/kristjanqarri" target="blank"><img align="center" src="./linked-in-alt.svg" alt="kristjanqarri" height="20" width="27" /></a> <a href="https://github.com/chrissMD" target="blank"><img align="center" src="./octocat.svg" alt="kristjanqarri" height="20" width="27" /></a><br>
**Pasquale Pellegrini** _(Team Leader)_: Biomedical scientist with a background in cancer research and neurodegeneration.<br>
<a href="https://www.linkedin.com/in/ppellegrini/" target="blank"><img align="center" src="./linked-in-alt.svg" alt="kristjanqarri" height="20" width="27" /></a> <a href="https://github.com/PasPelle" target="blank"><img align="center" src="./octocat.svg" alt="kristjanqarri" height="20" width="27" /></a>
<!--[![GitHub](https://img.shields.io/badge/GitHub-chrissMD-blue)](https://github.com/chrissMD) [![LinkedIn](https://img.shields.io/badge/LinkedIn-ppellegrini-blue)](https://www.linkedin.com/in/ppellegrini/)-->
# BACKGROUND
This project aims to leverage the pre-trained VGG16 Convolutional Neural Network on the ImageNet database. In addition dense and prediction layers are added to perform image classification in the healthy and metastasis classes.

# WORKFLOW

1. Selected a balanced subset of 2000 images from each class for training, with a 50:50 distribution.
2. Pre-processed (normalized) images were then input into the VGG16 network.
3. We developed an API using FastAPI and deployed the model as a web app using Streamlit.

# APPLICATION

Our Streamlit app is a user-friendly platform designed for histopathologic cancer detection. We've tailored it to enable users to upload histopathologic images in
specifically in 'tif' or 'tiff' file formats and receive accurate predictions regarding the presence of cancer. The app is enhanced with HTML styling for better visual appeal and offers an intuitive interface for ease of use. Key features of our app include:

1. Image Analysis and Prediction: Users can request a prediction upon uploading an image. Our app uses a backend API to analyze the image and return a cancer prediction.
2. Progress Feedback: We provide a progress bar and spinner, offering visual feedback during the image processing phase.
3. Result Display with Accessibility in Mind: The app displays the prediction results in colors specifically chosen to be friendly to the visually impaired, distinguishing between malignant (displayed in a visually distinct red) and non-malignant results (shown in a clear green), accompanied by probability scores.
4. Error Handling: We have integrated error messages for different scenarios, such as errors in prediction or API request failures.
5. User-Friendly Design: Our use of HTML - styled text ensures clear and large font displays, enhancing the overall user experience.

# LINKS

**API**: https://mlvscancer4.streamlit.app/ <br>
**Web application**: https://imageanalysis-ulbdrxxy6a-ew.a.run.app/predict_image <br>
**Image to test prediction**: [Image](./raw_data/team.jpg)<br>
_note: Download the .TIFF image from the link above to test the prediction of the model_

# FUTURE PERSPECTIVES

1. Extend the scope of our project to predict various types of primary cancers using a single urine test.
2. Explore the potential of the existing models to detect different cancer types and implement necessary adaptations to accommodate diverse cancer profiles.
3. Focus on creating a globally accessible primary cancer prediction application by incorporating language localization, adapting to different healthcare systems, and addressing specific regional healthcare needs and challenges.
4. Develop educational resources and materials to raise awareness about the importance of early cancer detection. Conduct outreach programs to educate the public, healthcare professionals, and relevant stakeholders about the benefits and capabilities of the primary cancer prediction app.

# CITATION

Will Cukierski. (2018). Histopathologic Cancer Detection. Kaggle. https://kaggle.com/competitions/histopathologic-cancer-detection

# KAGGLE COMPETITION
https://www.kaggle.com/competitions/histopathologic-cancer-detection
