import pandas as pd
import matplotlib.pylab as plt
from statsmodels.tsa.ar_model import AR
from sklearn.model_selection import train_test_split
from sain2021_g7.pipelines.evaluation.evaluation import evaluate
import warnings

warnings.filterwarnings("ignore")


def auto_regressor(df_train, df_test, data, target):

    data = data.drop(data.columns.difference([target, "date"]), 1)
    data["stationary"] = data[target].diff()

    X = data["stationary"].dropna()
    # train is now 75% of the entire dataset
    df_train = X[1 : len(X) - 12]
    df_test = X[len(X) - 12 :]

    # train the autoregression model
    model = AR(df_train)
    model_fitted = model.fit()

    # make predictions
    predictions = model_fitted.predict(
        start=len(df_train), end=len(df_train) + len(df_test) - 1, dynamic=False
    )

    # create a comparison dataframe
    compare_df = pd.concat([data["stationary"], predictions], axis=1).rename(
        columns={"stationary": "actual", 0: "predicted"}
    )

    # plot the two values
    compare_df.plot()

    eval = evaluate(data["stationary"].tail(12), predictions)
    eval_df = pd.DataFrame([eval], columns=eval.keys()).round(3)
    eval_df["target"] = target

    return eval_df
