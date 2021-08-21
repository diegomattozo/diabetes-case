import pickle
import pandas as pd
from diabetes.params import Params


def run(params: Params, data: pd.DataFrame) -> pd.DataFrame:
    """Run dataprep node

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
    data = model_obj["transformers"].transform(data)
    return data
