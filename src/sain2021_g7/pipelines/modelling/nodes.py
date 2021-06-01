# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This is a boilerplate pipeline 'modelling'
generated using Kedro 0.17.2
"""
import pandas as pd
from typing import Dict, List


def train_test_split(prodsales: pd.DataFrame, parameters: Dict) -> List:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.modelling import train_test_split

    return train_test_split(prodsales, parameters)


def multi_layer_perceptron(
    prod_sales_train: pd.DataFrame, prod_sales_test: pd.DataFrame, target: str
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.multi_layer_perceptron import (
        multi_layer_perceptron,
    )

    return multi_layer_perceptron(prod_sales_train, prod_sales_test, target)


def auto_regressor(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.auto_regressor import auto_regressor

    return auto_regressor(prod_sales_train, prod_sales_test, prod_sales, target)

def auto_arima(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.auto_arima import auto_arima

    return auto_arima(prod_sales_train, prod_sales_test, prod_sales, target)

def sarimax(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.sarimax import sarimax

    return sarimax(prod_sales_train, prod_sales_test, prod_sales, target)

def var(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.var import var

    return auto_regressor(prod_sales_train, prod_sales_test, prod_sales, target)


def moving_average(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.moving_average import moving_average

    return moving_average(prod_sales_train, prod_sales_test, prod_sales, target)

def holt_winters(
    prod_sales_train: pd.DataFrame,
    prod_sales_test: pd.DataFrame,
    prod_sales,
    target: str,
) -> pd.DataFrame:
    """Node to split dataset into train and test dataset for further
    model trainning.

    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Train and test data
    """
    from sain2021_g7.pipelines.modelling.holt_winters import holt_winters

    return holt_winters(prod_sales_train, prod_sales_test, prod_sales, target)


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
    from sain2021_g7.pipelines.modelling.modelling import concat
    return concat(results_pporto, 
                     results_pguima, 
                     results_sporto, 
                     results_spovoa, 
                     results_sbarce, 
                     results_sfama, 
                     results_sbraga, 
                     results_sguima)