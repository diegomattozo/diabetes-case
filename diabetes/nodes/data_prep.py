import pickle


def run(params, data):

    with open(params.model_path, "rb") as f:
        model_obj = pickle.loads(f.read())
    data = model_obj["transformers"].transform(data)
    return data
