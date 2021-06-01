import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os

from typing import Dict, List


def data_exploration(prod_sales_date_range: pd.DataFrame, parameters: Dict):
    """Node to draw a line plot with x as the timeframe, column "date"
    and y as the rows of the data according to the timeframe. This
    node will create a n number of plots based on the columns of
    the dataset and defined in parameters.

    Args:
        prod_sales_date_range (pd.DataFrame): Production and Sales data with date range
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        Data exploration of the columns in the data defined as targets in parameters
    """
    _targets = parameters["targets"]
    _path = parameters["paths"]["exploration_folder"]

    prod_sales_date_range["date"] = pd.to_datetime(
        prod_sales_date_range["date"], infer_datetime_format=True
    )

    if not os.path.exists(_path):
        os.makedirs(_path)

    sns.set_theme(style="darkgrid")
    for t in _targets:
        plt.subplots(figsize=(10, 4))
        sns.lineplot(x="date", y=t, color="#F77737", data=prod_sales_date_range)
        plt.xlabel='Data'
        plt.ylabel=f"Quantidade: {t}"
        plt.savefig(f"{_path}/{t}.svg")

    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)

    return df

paths = [".data/"]
