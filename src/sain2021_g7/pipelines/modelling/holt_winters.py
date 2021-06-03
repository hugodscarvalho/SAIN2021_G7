import pandas as pd 
from numpy import mean
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sain2021_g7.pipelines.evaluation.evaluation import evaluate
import os 
import seaborn as sns
import matplotlib.pyplot as plt

# prepare situation

def holt_winters(df_train, df_test, data, target):

    hwmodel=ExponentialSmoothing(df_train[target], trend='add', seasonal='mul', seasonal_periods=len(df_test)).fit()
    
    test_pred=hwmodel.forecast(len(df_test))

    # metrics = evaluate(test, predictions)
    metrics = evaluate(df_test[target].to_numpy(), test_pred.to_numpy())

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target

    _path = 'data/09_plots/holt_winters'

    if not os.path.exists(_path):
        os.makedirs(_path)

    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10,5))
    plt.plot(df_train[target],label="Training")
    plt.plot(df_test,label="Test")
    plt.plot(test_pred,label="Predicted")
    plt.legend(loc = 'upper right')
    plt.savefig(f"{_path}/{target}.svg")

    
    return eval_df