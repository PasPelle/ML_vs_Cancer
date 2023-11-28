from mlflow.tracking import MlflowClient
from tensorflow import keras
from keras import Sequential, Model
from typing import Tuple
import numpy as np

def initialize_model() -> Model:
    """
    Initialize the Neural Network with random weights
    """
    # TODO add layers
    model = Sequential()
    return model

def compile_model(model: Model) -> Model:
    """
    Compile the Neural Network
    """
    # TODO add compiling
    return model

def train_model(model: Model, X: np.ndarray, y: np.ndarray) -> Tuple[Model, dict]:
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    # TODO train the model
    history = None
    return model, history

def evaluate_model(model: Model, X: np.ndarray, y: np.ndarray) -> Tuple[Model, dict]:
    """
    Evaluate trained model performance on the dataset
    """
    # TODO evaluate the model
    metrics = None
    return metrics