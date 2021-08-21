import pickle
import numpy as np
import pandas as pd
from diabetes.params import Params


def run(params: Params, data: pd.DataFrame) -> pd.DataFrame:
    """Apply threshold in model score

    Parameters
    ----------
    params : Params
        Model spec
    data : pd.DataFrame
        DataFrame to apply dataprep

    Returns
    -------
    pd.DataFrame
        New DataFrame after running this node
    """
    with open(params.model_path, "rb") as f:
        model_obj = pickle.loads(f.read())
    resp = np.where(data["score"] > model_obj["cutpoint"], 1, 0)
    data["class_estimada"] = resp
    return data
