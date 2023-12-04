from fastapi import FastAPI, File, UploadFile
import pandas as pd
#from fastapi.middleware.cors import CORSMiddleware
from ML_vs_Cancer.ml_logic.registry import load_model
from ML_vs_Cancer.ml_logic import read_tiff_image
import numpy as np
from PIL import Image
from io import BytesIO

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
        
        
@app.post("/predict_image")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
        contents = await file.read()
        image = Image.open(BytesIO(contents)).convert("RGB")
        
        expanded_array_img = np.expand_dims(image, axis=0)
        prediction = app.state.model.predict(expanded_array_img)
        res = round(float(prediction[0][0]), 4)
        return {"Prediction": res}
