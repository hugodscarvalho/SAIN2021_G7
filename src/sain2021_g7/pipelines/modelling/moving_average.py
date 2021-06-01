from numpy.core.fromnumeric import shape
import pandas as pd 
from numpy import mean
from sain2021_g7.pipelines.evaluation.evaluation import evaluate

# prepare situation
def moving_average(df_train, df_test, data, target):

    X = data[target].values
    window = 3
    history = [X[i] for i in range(window)]
    test = [X[i] for i in range(window, len(X))]
    predictions = list()
    # walk forward over time steps in test
    for t in range(len(test)):
        length = len(history)
        yhat = mean([history[i] for i in range(length-window,length)])
        obs = test[t]
        predictions.append(yhat)
        history.append(obs)
        # print('predicted=%f, expected=%f' % (yhat, obs))
    
    _test = pd.Series(test)
    _predictions = pd.Series(predictions)
    print("Predictions:", predictions)
    print("Test:", test)
    # metrics = evaluate(test, predictions)
    metrics = evaluate(_test.to_numpy(), _predictions.to_numpy())

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df