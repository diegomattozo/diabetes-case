from typing import Dict, List, Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureAdder(BaseEstimator, TransformerMixin):
    """Adds new features to dataset"""

    def __init__(self) -> None:
        ...

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "FeatureAdder":
        """Fit method

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to transform
        y : pd.Series
            Target column
        Returns
        -------
        FeatureAdder
            Self
        """
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Add proportion of main symptoms and female with peak age columns

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to transform

        Returns
        -------
        pd.DataFrame
            Transformed Dataframe
        """
        _X = X.copy()
        _X = self._main_symptoms(_X)
        _X = self._female_peak_age(_X)
        return _X

    def _main_symptoms(self, data: pd.DataFrame) -> pd.DataFrame:
        has_polyuria = np.where(data.polyuria == "Yes", 1, 0)
        has_polydipsia = np.where(data.polydipsia == "Yes", 1, 0)
        has_polyphagia = np.where(data.polyphagia == "Yes", 1, 0)
        has_sudden_weight_loss = np.where(data.sudden_weight_loss == "Yes", 1, 0)
        has_partial_paresis = np.where(data.partial_paresis == "Yes", 1, 0)
        has_polyphagia = np.where(data.polyphagia == "Yes", 1, 0)
        data["prop_main_symptoms_6"] = (
            has_polyuria
            + has_polydipsia
            + has_polyphagia
            + has_sudden_weight_loss
            + has_partial_paresis
            + has_polyphagia
        ) / 6
        data["prop_main_symptoms_3"] = (
            has_polyuria + has_polydipsia + has_sudden_weight_loss
        ) / 3
        return data

    def _female_peak_age(self, data: pd.DataFrame) -> pd.DataFrame:
        has_age_31_40 = (data.age >= 31) & (data.age <= 40)
        has_age_46_55 = (data.age >= 46) & (data.age <= 55)
        has_age = has_age_31_40 | has_age_46_55
        is_female = data.gender == "Female"
        data["is_female_with_peak_age"] = np.where(is_female & has_age, 1, 0)
        return data


class CategoricalConverter(BaseEstimator, TransformerMixin):
    """Convert categorical to numerical representation"""

    def __init__(self) -> None:
        self.columns: List[str] = []
        self.categ_mapping: Dict[str, np.ndarray] = {}

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> "CategoricalConverter":
        """Fit method, initialize columns with own unique values

        Parameters
        ----------
        X : pd.DataFrame
            Data to transform
        y : pd.Series, optional
            Target column, by default None

        Returns
        -------
        CategoricalConverter
            Self
        """
        self.columns = [col for col in X.columns]
        self.categ_mapping = self._col_mapping(X)
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Converting nominal columns to integer type

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to transform

        Returns
        -------
        pd.DataFrame
            Transformed Dataframe
        """
        _X = X.copy()
        for col in self.columns:
            _X[col] = pd.Categorical(_X[col], categories=self.categ_mapping[col]).codes
        return _X

    def _col_mapping(self, data):
        columns = data.columns
        col_mapping = {}
        for col in columns:
            col_mapping[col] = list(np.unique(data[col]))
        return col_mapping
