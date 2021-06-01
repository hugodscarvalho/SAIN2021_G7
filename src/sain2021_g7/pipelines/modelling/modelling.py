import pandas as pd
import numpy as np
from typing import Dict, List


def train_test_split(prodsales: pd.DataFrame, parameters: Dict) -> List:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    train_ratio = parameters["train_ratio"]
    start_test = len(prodsales) - int(train_ratio * len(prodsales))

    prodsales_train = prodsales[:-start_test]
    prodsales_test = prodsales[-start_test:]

    return prodsales_train, prodsales_test


def concat(results_pporto: pd.DataFrame, 
                     results_pguima: pd.DataFrame, 
                     results_sporto: pd.DataFrame, 
                     results_spovoa: pd.DataFrame, 
                     results_sbarce: pd.DataFrame, 
                     results_sfama: pd.DataFrame, 
                     results_sbraga: pd.DataFrame, 
                     results_sguima: pd.DataFrame) -> pd.DataFrame:
    """Node to concatenate results of the targets

    Args:
        results_pporto (pd.DataFrame): [description]
        results_pguima (pd.DataFrame): [description]
        results_sporto (pd.DataFrame): [description]
        results_spovoa (pd.DataFrame): [description]
        results_sbarce (pd.DataFrame): [description]
        results_sfama (pd.DataFrame): [description]
        results_sbraga (pd.DataFrame): [description]
        results_sguima (pd.DataFrame): [description]

    Returns:
        pd.DataFrame: [description]
    """
    frames = [results_pporto, results_pguima, results_sporto, results_spovoa, results_sbarce, results_sfama, results_sbraga, results_sguima]

    result = pd.concat(frames)

    return result