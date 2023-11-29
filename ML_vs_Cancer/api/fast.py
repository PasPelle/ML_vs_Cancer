from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io

import pandas as pd
#from fastapi.middleware.cors import CORSMiddleware
from ML_vs_Cancer.ml_logic.registry import load_model
from ML_vs_Cancer.ml_logic import read_tiff_image

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
# def predict(f1 , f2, f3, f4, f5):
#     #X_pred = pd.DataFrame(locals(), index=[0])
#     x_dict = {
#         "f1": float(f1),
#         "f2": float(f2),
#         "f3": float(f3),
#         "f4": float(f4),
#         "f5": float(f5)
#     }
#     X_pred = pd.DataFrame(x_dict, index=[0])
#     model = app.state.model
#     y_pred = model.predict(X_pred)
#     #return {'Predict': "Hello ML vs Cancer"}
#     return dict(prediction=float(y_pred))
@app.post("/process_tiff/")
def process_tiff(file: UploadFile = File(...)):
    try:
        image_array = read_tiff_image(file)
        res = app.state.model(image_array)
        if res == 1:
            return {"Prediction": "Malign"}
        else:
            return {"Prediction": "Bennign"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
