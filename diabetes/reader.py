import pandas as pd
import numpy as np


def read_data(path: str, sep=","):
    data = pd.read_csv(path, sep=sep)
    # removendo espaços dos nomes das colunas e colocando tudo minusculo
    data.columns = [col.lower() for col in data.columns]
    data.columns = ["_".join(col.split()) for col in data.columns]
    data["class"] = np.where(data["class"] == "Positive", 1, 0)
    return data
