import pickle
import pandas as pd
from diabetes.params import Params


def run(params: Params, data: pd.DataFrame) -> pd.DataFrame:
    """Score model

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
    data["score"] = model_obj["model"].predict_proba(data[model_obj["columns"]])[:, 1]
    return data
