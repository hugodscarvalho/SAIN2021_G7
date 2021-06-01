
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') 
from statsmodels.tsa.vector_ar.var_model import VAR
from sain2021_g7.pipelines.evaluation.evaluation import evaluate



def var(df_train, df_test, data, target):

    #diff
    diff_df = data[target].diff()

    #fit the model
    model = VAR(endog=df_train)
    model_fit = model.fit()

    # make prediction on validation
    prediction = model_fit.forecast(model_fit.y, steps=len(df_test))

    #converting predictions to dataframe
    pred = pd.DataFrame(index=range(0,len(prediction)),columns=[target])
 
    metrics = evaluate(df_test[target], pred)

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df