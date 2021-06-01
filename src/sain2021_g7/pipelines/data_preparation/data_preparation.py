import pandas as pd
import numpy as np
from typing import Dict, List

# from sdv.evaluation import evaluate
# from sdv.tabular import CTGAN, GaussianCopula

from sklearn.preprocessing import StandardScaler


def linear_interpolation(prodsales: pd.DataFrame) -> pd.DataFrame:
    """Node to fill missing values in raw data using linear interpolation.
    With this technique unknown data points between two known data points can estimated.
    The direction of filling of values will be forward.
    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Production and Sales data with missing values filled
    """
    # Use linear interpolation to fill missing data
    prodsales.interpolate(method="linear", limit_direction="forward", inplace=True)
    # Round entire DataFrame to 0 decimals once linear interpolation will generate float type and convert it to int
    _prodsales = prodsales.copy()
    _prodsales = prodsales.round(0).astype(int)

    return _prodsales


def ctgan_synthetic_generator(
    prod_sales_filled: pd.DataFrame, parameters: Dict
) -> List:
    """Node to generate synthetic data using a CTGAN. The sdv.tabular. CTGAN model is based
    on the GAN-based Deep Learning data synthesizer which was presented at the NeurIPS
    2020 conference by the paper titled Modeling Tabular data using Conditional GAN.
    Args:
        prod_sales_filled (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        List: List of pandas DataFrames: Production and Sales synthetic data and
        and the evaluation of the synthetic data.
    """
    model = CTGAN()
    model.fit(prod_sales_filled)

    rows = parameters["synthetic_data"]["CTGAN"]["rows"]
    ctgan_synthetic_data = model.sample(rows)
    ctgan_eval = evaluate(ctgan_synthetic_data, prod_sales_filled, aggregate=False)
    ctgan_synthetic_data = ctgan_synthetic_data.round(0).astype(int)

    return ctgan_synthetic_data, ctgan_eval


def gaussian_copula_synthetic_generator(
    prod_sales_filled: pd.DataFrame, parameters: Dict
) -> List:
    """Node to generate synthetic data using a GaussianCopula. Intuitively, a copula is a mathematical
    function that allows us to describe the joint distribution of multiple random variables by
    analyzing the dependencies between their marginal distributions.
    Args:
        prod_sales_filled (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        List: List of pandas DataFrames: Production and Sales synthetic data and
        and the evaluation of the synthetic data.
    """
    model = GaussianCopula()
    model.fit(prod_sales_filled)

    rows = parameters["synthetic_data"]["GaussianCopula"]["rows"]
    gaussian_copula_synthetic_data = model.sample(rows)
    gc_eval = evaluate(
        gaussian_copula_synthetic_data, prod_sales_filled, aggregate=False
    )
    gaussian_copula_synthetic_data = gaussian_copula_synthetic_data.round(0).astype(int)

    return gaussian_copula_synthetic_data, gc_eval


def add_date_range(prod_sales_filled: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """Node to add a date range to the data using date_range(), one of the general functions
    in Pandas which is used to return a fixed frequency DatetimeIndex

    Args:
        prod_sales_filled (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        pd.DataFrame: Production and Sales data with date range
    """
    end_date = parameters["time"]["end_date"]
    frequency = parameters["time"]["frequency"]

    prod_sales_date_range = prod_sales_filled.copy()
    prod_sales_date_range["date"] = pd.date_range(
        end=end_date, periods=len(prod_sales_filled), freq=frequency
    )

    return prod_sales_date_range
