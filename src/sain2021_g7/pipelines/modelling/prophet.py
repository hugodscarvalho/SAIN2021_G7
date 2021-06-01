


def sarimax(df_train, df_test, data, target):

  
    df = df[['date', p]].dropna()
    df = df.set_index('date')
    daily_df = df.resample('M').mean()
    d_df = daily_df.reset_index().dropna()

    d_df.columns = ['ds', 'y']
    fig = plt.figure(facecolor='w', figsize=(10, 5))
    #plt.plot(d_df.ds, d_df.y)
    m = Prophet()
    m.fit(d_df)
    train=df[-37:]
    ano = 2
    periods = ano * 12
    future = m.make_future_dataframe(periods=periods,  freq = 'M')
    #print(future)
    forecast = m.predict(future)
    forecast[['ds', 'yhat']].tail()
    forecast=forecast[-37:]
    forecast.index = forecast.ds
    forecast = forecast.drop(['ds'], axis=1)
    forecast = forecast['yhat']

    print(forecast)

    metrics = evaluate(df_test[target].to_numpy(), predictions.to_numpy())

    eval_df = pd.DataFrame([metrics], columns=metrics.keys()).round(3)
    eval_df["target"] = target    
    
    return eval_df