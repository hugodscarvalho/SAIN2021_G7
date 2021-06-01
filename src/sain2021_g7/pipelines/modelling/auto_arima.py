import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') 
from pmdarima.arima import auto_arima as ar
from sain2021_g7.pipelines.evaluation.evaluation import evaluate


def auto_arima(df_train, df_test, data, target):

    arima_model =  ar(df_train[target], start_p=0, d=1, start_q=0, 
                          max_p=5, max_d=5, max_q=5, start_P=0, 
                          D=1, start_Q=0, max_P=5, max_D=5,
                          max_Q=5, m=12, seasonal=True, 
                          error_action='warn',trace = True,
                          supress_warnings=True,stepwise = True,
                          random_state=20,n_fits = 50 )

    prediction = pd.DataFrame(arima_model.predict(n_periods = len(df_test)),index=df_test.index)
    prediction.columns = ['predicted_sales']
    #prediction.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    metrics = evaluate(df_test[target], prediction["predicted_sales"])
    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    

    return eval_df
