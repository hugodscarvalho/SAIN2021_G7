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

from kedro.config import ConfigLoader
from kedro.pipeline import Pipeline, node
from .nodes import holt_winters, train_test_split, multi_layer_perceptron, auto_regressor,auto_arima, sarimax, VAR, moving_average, holt_winters, Prophet, LSTM, concat


# def create_pipeline(**kwargs):

#     return Pipeline([
#         node(
#             func=train_test_split,
#             inputs=["prod_sales_date_range", "parameters"],
#             outputs=["prod_sales_train", "prod_sales_test"],
#             tags="split",
#             ),
#         node(
#             func=multi_layer_perceptron,
#             inputs=["prod_sales_train", "prod_sales_test", "parameters"],
#             outputs="results_mlp",
#             tags="multi_layer_perceptron",
#             ),
#         ])


def create_pipeline(**kwargs):
    conf_paths = ["conf/base", "conf/local"]
    conf_loader = ConfigLoader(conf_paths)
    parameters = conf_loader.get("parameters*", "parameters*/**")
    TARGETS = parameters["targets"]

    pipeline_list = []

    pipeline_list.append(
        node(
            func=train_test_split,
            inputs=["prod_sales_date_range", "parameters"],
            outputs=["prod_sales_train", "prod_sales_test"],
            tags="split",
        ),
    )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_MLP",
                func=multi_layer_perceptron,
                inputs=["prod_sales_train", "prod_sales_test", f"params:{t}"],
                outputs=f"results_mlp_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_AR",
                func=auto_regressor,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_ar_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_AUTO_ARIMA",
                func=auto_arima,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_auto_arima_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_SARIMAX",
                func=sarimax,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_sarimax_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_VAR",
                func=VAR,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_var_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_moving_average",
                func=moving_average,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_moving_average_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_holt_winters",
                func=holt_winters,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_holt_winters_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_prophet",
                func=Prophet,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_prophet_{t}",
                tags=["encode"],
            )
        )
    for idx, t in enumerate(TARGETS):
        pipeline_list.append(
            node(
                name=f"{t}_lstm",
                func=LSTM,
                inputs=[
                    "prod_sales_train",
                    "prod_sales_test",
                    "prod_sales_date_range",
                    f"params:{t}",
                ],
                outputs=f"results_lstm_{t}",
                tags=["encode"],
            )
        )
    MODELS= ["mlp", "ar", "auto_arima", "sarimax", "holt_winters", "svr", "prophet", "var", "moving_average", "lstm"]
    for idx, m in enumerate(MODELS):
        pipeline_list.append(
            node(
                name=f"Concatenate_{m}",
                func=concat,
                inputs=[f"results_{m}_pporto", f"results_{m}_pguima", f"results_{m}_sporto", f"results_{m}_spovoa", f"results_{m}_sbarce", f"results_{m}_sfama", f"results_{m}_sbraga", f"results_{m}_sguima"],
                outputs=f"concat_results_{m}",
                tags=["encode"],
            )
        )
    

    return Pipeline(pipeline_list)
