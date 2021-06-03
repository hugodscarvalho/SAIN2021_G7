from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
import pandas as pd
from matplotlib import pyplot
from sain2021_g7.pipelines.evaluation.evaluation import evaluate


def prophet(df_train, df_test, data, target):

    data = data[['date', target]]
    data['date'] = pd.to_datetime(data['date'])

    data = data.set_index('date')

    df = data.resample('D').mean()
    df = df.reset_index().dropna()
    df.columns = ['ds', 'y']

    df = df.rename({'date': 'ds', target : 'y'}, axis=1)  # new method
    
    df_train = df_train[['date', target]]
    df_train = df_train.rename({'date': 'ds', target : 'y'}, axis=1)  # new method

    df_test = df_test[['date', target]]
    df_test = df_test.rename({'date': 'ds', target : 'y'}, axis=1)  # new method

    m = Prophet()
    m.fit(df_train)

    predictions = m.predict(df_test)

    #prediction.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    metrics = evaluate(df_test['y'].to_numpy(), predictions['yhat'].to_numpy())
    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df
    