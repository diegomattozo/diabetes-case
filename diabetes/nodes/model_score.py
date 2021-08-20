import pickle


def run(params, data):
    with open(params.model_path, "rb") as f:
        model_obj = pickle.loads(f.read())
    data["score"] = model_obj["model"].predict_proba(data[model_obj["columns"]])[:, 1]
    return data
