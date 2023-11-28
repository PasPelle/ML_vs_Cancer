from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# app.state.model = load_model()

# A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def root():
    return {'Root': "Hello ML vs Cancer"}

@app.get("/predict")
def predict():
    return {'Predict': "Hello ML vs Cancer"}
