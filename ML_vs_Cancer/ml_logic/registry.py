from tensorflow import keras
#from keras import Model

from google.cloud import storage
import os
import glob
import time
import pickle

from colorama import Fore, Style

from ML_vs_Cancer.params import *
#from tensorflow.keras.models import load_model

def load_model() -> keras.Model:
    """
    Return a saved model:
    - locally (latest one in alphabetical order)
    - or from GCS (most recent one) if MODEL_TARGET=='gcs'  --> for unit 02 only

    Return None (but do not Raise) if no model is found

    """
    # if MODEL_TARGET == "local":
    #     # Get the latest model version name by the timestamp on disk
    #     local_model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")
    #     local_model_paths = glob.glob(f"{local_model_directory}/*")

    #     if not local_model_paths:
    #         return None

    #     most_recent_model_path_on_disk = sorted(local_model_paths)[-1]

    #     latest_model = keras.models.load_model(most_recent_model_path_on_disk)

    #     return latest_model
    # elif MODEL_TARGET == "gcs":
    #     client = storage.Client()
    #     blobs = list(client.get_bucket(BUCKET_NAME).list_blobs(prefix="model"))

    #     try:
    #         latest_blob = max(blobs, key=lambda x: x.updated)
    #         latest_model_path_to_save = os.path.join(LOCAL_REGISTRY_PATH, latest_blob.name)
    #         latest_blob.download_to_filename(latest_model_path_to_save)

    #         latest_model = keras.models.load_model(latest_model_path_to_save)

    #         return latest_model
    #     except:
    #         return None
    # elif MODEL_TARGET == "github":
    model = keras.models.load_model(
        'raw_data/baseline_model.h5',
        compile=False)
    return model
    # else:
    #     return None

def save_model(model: keras.Model = None) -> None:
    """
    Persist trained model locally on the hard drive at f"{LOCAL_REGISTRY_PATH}/models/{timestamp}.h5"
    - if MODEL_TARGET='gcs', also persist it in your bucket on GCS at "models/{timestamp}.h5" --> unit 02 only
   """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Save model locally
    model_path = os.path.join(LOCAL_REGISTRY_PATH, "models", f"{timestamp}.h5")
    model.save(model_path)

    if MODEL_TARGET == "gcs":

        model_filename = model_path.split("/")[-1] # e.g. "20230208-161047.h5" for instance
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(f"models/{model_filename}")
        blob.upload_from_filename(model_path)

        return None
    return None

def save_results(params: dict, metrics: dict) -> None:
    """
    Persist params & metrics locally on the hard drive at
    "{LOCAL_REGISTRY_PATH}/params/{current_timestamp}.pickle"
    "{LOCAL_REGISTRY_PATH}/metrics/{current_timestamp}.pickle"
    - (unit 03 only)
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Save params locally
    if params is not None:
        params_path = os.path.join(LOCAL_REGISTRY_PATH, "params", timestamp + ".pickle")
        with open(params_path, "wb") as file:
            pickle.dump(params, file)

    # Save metrics locally
    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics", timestamp + ".pickle")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)
