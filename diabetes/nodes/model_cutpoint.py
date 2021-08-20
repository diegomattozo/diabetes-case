import pickle
import numpy as np


def run(params, data):
    with open(params.model_path, "rb") as f:
        model_obj = pickle.loads(f.read())
    resp = np.where(data["score"] > model_obj["cutpoint"], 1, 0)
    data["class_estimada"] = resp
    return data
