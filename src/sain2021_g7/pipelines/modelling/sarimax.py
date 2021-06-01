import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') 
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sain2021_g7.pipelines.evaluation.evaluation import evaluate


def sarimax(df_train, df_test, data, target):

    model = SARIMAX(df_train[target], 
                    order = (0, 1, 1), 
                    seasonal_order =(2, 1, 1, 12))
    
    result = model.fit()
    result.summary()


    start = len(df_train)
    end = len(df_train) + len(df_test) - 1
    
    # Predictions for one-year against the test set
    predictions = result.predict(start, end,
                                typ = 'levels').rename("Predictions")

    print(type(predictions))
    metrics = evaluate(df_test[target].to_numpy(), predictions.to_numpy())

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df