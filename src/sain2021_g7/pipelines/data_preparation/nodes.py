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
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.17.2
"""
import pandas as pd
from typing import Dict, List


def linear_interpolation(prodsales: pd.DataFrame) -> pd.DataFrame:
    """Node to fill missing values in raw data using linear interpolation.
    With this technique unknown data points between two known data points can estimated.
    The direction of filling of values will be forward.
    Args:
        prodsales (pd.DataFrame): Production and Sales data

    Returns:
        pd.DataFrame: Production and Sales data with missing values filled
    """
    from sain2021_g7.pipelines.data_preparation.data_preparation import (
        linear_interpolation,
    )

    return linear_interpolation(prodsales)


def add_date_range(prodsales_filled: pd.DataFrame, parameters: Dict) -> pd.DataFrame:
    """Node to add a date range to the data using date_range(), one of the general functions
    in Pandas which is used to return a fixed frequency DatetimeIndex

    Args:
        prod_sales_filled (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        pd.DataFrame: Production and Sales data with date range
    """
    from sain2021_g7.pipelines.data_preparation.data_preparation import add_date_range

    return add_date_range(prodsales_filled, parameters)


def standardize(prod_sales_date_range: pd.DataFrame) -> List:
    """Node to standardize the data using the library StandardScaler
    from the sklearn.preprocessing. This method standardizes features
    by removing the mean and scaling to unit variance

    Args:
        prod_sales_date_range (pd.DataFrame): Training data

    Returns:
        List: Production and Sales data and the used scaler as joblib.
    """
    from sain2021_g7.pipelines.data_preparation.data_preparation import standardize

    return standardize(prod_sales_date_range)


def ctgan_synthetic_generator(prodsales_filled: pd.DataFrame, parameters: Dict) -> List:
    """Node to generate synthetic data using a CTGAN. The sdv.tabular. CTGAN model is based
    on the GAN-based Deep Learning data synthesizer which was presented at the NeurIPS
    2020 conference by the paper titled Modeling Tabular data using Conditional GAN.
    Args:
        prodsales (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        List: List of pandas DataFrames: Production and Sales synthetic data and
        and the evaluation of the synthetic data.
    """
    from sain2021_g7.pipelines.data_preparation.data_preparation import (
        ctgan_synthetic_generator,
    )

    return ctgan_synthetic_generator(prodsales_filled, parameters)


def gaussian_copula_synthetic_generator(
    prodsales_filled: pd.DataFrame, parameters: Dict
) -> List:
    """Node to generate synthetic data using a GaussianCopula. Intuitively, a copula is a mathematical
    function that allows us to describe the joint distribution of multiple random variables by
    analyzing the dependencies between their marginal distributions.
    Args:
        prodsales (pd.DataFrame): Production and Sales data filled
        parameters (Dict): Parameters defined in parameters.yml

    Returns:
        List: List of pandas DataFrames: Production and Sales synthetic data and
        and the evaluation of the synthetic data.
    """
    from sain2021_g7.pipelines.data_preparation.data_preparation import (
        gaussian_copula_synthetic_generator,
    )

    return gaussian_copula_synthetic_generator(prodsales_filled, parameters)
