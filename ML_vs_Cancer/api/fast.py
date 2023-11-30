from fastapi import FastAPI, File, UploadFile
import pandas as pd
#from fastapi.middleware.cors import CORSMiddleware
from ML_vs_Cancer.ml_logic.registry import load_model
from ML_vs_Cancer.ml_logic import read_tiff_image
import numpy as np
import cv2
app = FastAPI()
app.state.model = load_model()

# A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )

@app.get("/")
def root():
    return {'Root': "Hello ML vs Cancer"}

@app.get("/predict")
def predict(f1 , f2, f3, f4, f5):
    #X_pred = pd.DataFrame(locals(), index=[0])
    x_dict = {
        "f1": float(f1),
        "f2": float(f2),
        "f3": float(f3),
        "f4": float(f4),
        "f5": float(f5)
    }
    X_pred = pd.DataFrame(x_dict, index=[0])
    y_pred = x_dict["f1"]**2
    #return {'Predict': "Hello ML vs Cancer"}
    return dict(prediction=float(y_pred))

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()
    # convert the raw byte content of the image into a NumPy array of 8-bit unsigned integers
    nparr = np.fromstring(contents, np.uint8)
    # to decode the NumPy array into an image.
    # The resulting cv2_img is a NumPy array representing the image in BGR color format.
    # The cv2.IMREAD_COLOR flag specifies that the image should be read in color.
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray
    cv2.imwrite("saved_img.tif",cv2_img)
    ### Do cool stuff with your image.... For example face detection
    # we dont ned this: annotated_img = annotate_face(cv2_img)

    ### Encoding and responding with the image
    retrieved_val, encoded_image = cv2.imencode('.png', nparr) # extension depends on which format is sent from Streamlit
    #return Response(content=im.tobytes(), media_type="image/png")
    if retrieved_val:
        #print("Encoding successful.")
        expanded_array_img = np.expand_dims(cv2_img, axis=0)
        prediction = app.state.model.predict(expanded_array_img)
        res = round(float(prediction[0][0]), 2)
        #print (res)
        return {"Prediction": res}
    else:
        print("Encoding Failed.")
