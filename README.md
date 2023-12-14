# TEAM

**Daniel Stark**
Background in 3D design … please write 1-3 sentences for yourself
> GitHub: [![GitHub](https://img.shields.io/badge/GitHub-drostark-blue)](https://github.com/drostark)
> Linkedin: [![LinkedIn](https://img.shields.io/badge/LinkedIn-dstark2022-blue)](https://www.linkedin.com/in/dstark2022/)

**Katažyna Balcevič**
Background in ..… please write 1-3 sentences for yourself
> GitHub: [![GitHub](https://img.shields.io/badge/GitHub-Katazynab-blue)](https://github.com/Katazynab)
> Linkedin: [![LinkedIn](https://img.shields.io/badge/LinkedIn-katazynabalcevic-blue)](https://www.linkedin.com/in/katazynabalcevic/)

**Kristjan Qarri** [![GitHub](https://img.shields.io/badge/GitHub-chrissMD-blue)](https://github.com/chrissMD) [![LinkedIn](https://img.shields.io/badge/LinkedIn-kristjanqarri-blue)](https://www.linkedin.com/in/kristjanqarri/)

Medical Technology Engineer & passionate about the application of technology in healthcare.

**Pasquale Pellegrini** _(Team Leader)_ Biomedical scientist with a background in cancer research and neurodegeneration.
> GitHub: [![GitHub](https://img.shields.io/badge/GitHub-chrissMD-blue)](https://github.com/chrissMD)
> Linkedin: [![LinkedIn](https://img.shields.io/badge/LinkedIn-ppellegrini-blue)](https://www.linkedin.com/in/ppellegrini/)

# BACKGROUND

# OBJECTIVE

This study aims to leverage the VGG16 Convolutional Neural Network trained on the ImageNet database to perform image classification in the healthy and metastasis classes.

# WORKFLOW

Selected a balanced subset of 2000 images from each class for training, with a 50:50 distribution.
Pre-processed (normalized) images were then input into the VGG16 network.
We developed an API using FastAPI and deployed the model as a web app using Streamlit.


# APPLICATION

Streamlit:
Our Streamlit app is a user-friendly platform designed for histopathologic cancer detection. We've tailored it to enable users to upload histopathologic images in
specifically in 'tif' or 'tiff' file formats and receive accurate predictions regarding the presence of cancer. The app is enhanced with HTML styling for better visual appeal and offers an intuitive interface for ease of use. Key features of our app include:

Image Analysis and Prediction: Users can request a prediction upon uploading an image. Our app uses a backend API to analyze the image and return a cancer prediction.
Progress Feedback: We provide a progress bar and spinner, offering visual feedback during the image processing phase.
Result Display with Accessibility in Mind: The app displays the prediction results in colors specifically chosen to be friendly to the visually impaired, distinguishing between malignant (displayed in a visually distinct red) and non-malignant results (shown in a clear green), accompanied by probability scores.
Error Handling: We have integrated error messages for different scenarios, such as errors in prediction or API request failures.
User-Friendly Design: Our use of HTML- styled text ensures clear and large font displays, enhancing the overall user experience.

API link

tiff images link

# FUTURE PERSPECTIVES

We want to:
Extend the scope of our project to predict various types of primary cancers using a single urine test.
Explore the potential of the existing models to detect different cancer types and implement necessary adaptations to accommodate diverse cancer profiles.
Focus on creating a globally accessible primary cancer prediction application by incorporating language localization, adapting to different healthcare systems, and addressing specific regional healthcare needs and challenges.
Develop educational resources and materials to raise awareness about the importance of early cancer detection. Conduct outreach programs to educate the public, healthcare professionals, and relevant stakeholders about the benefits and capabilities of the primary cancer prediction app.

# CITATION

Will Cukierski. (2018). Histopathologic Cancer Detection. Kaggle. https://kaggle.com/competitions/histopathologic-cancer-detection
