import pandas as pd 
from numpy import mean
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sain2021_g7.pipelines.evaluation.evaluation import evaluate

# prepare situation
def holt_winters(df_train, df_test, data, target):

    hwmodel=ExponentialSmoothing(df_train[target], trend='add', seasonal='mul', seasonal_periods=len(df_test)).fit()
    
    test_pred=hwmodel.forecast(len(df_test))

    # metrics = evaluate(test, predictions)
    metrics = evaluate(df_test[target].to_numpy(), test_pred.to_numpy())

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df