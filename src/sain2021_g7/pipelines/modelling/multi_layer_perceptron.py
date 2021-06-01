from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sain2021_g7.pipelines.evaluation.evaluation import evaluate

# transform list into supervised learning format
def series_to_supervised(data, n_in=1, n_out=1):
	df = pd.DataFrame(data)
	cols = list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
	# put it all together
	agg = pd.concat(cols, axis=1)
	# drop rows with NaN values
	agg.dropna(inplace=True)
	return agg.values
 
# fit a model
def model_fit(train, config):
	# unpack config
	n_input, n_nodes, n_epochs, n_batch = config
	# prepare data
	data = series_to_supervised(train, n_in=n_input)
	train_x, train_y = data[:, :-1], data[:, -1]
	# define model
	model = Sequential()
	model.add(Dense(n_nodes, activation='relu', input_dim=n_input))
	model.add(Dense(1))
	model.compile(loss='mse', optimizer='adam')
	# fit
	model.fit(train_x, train_y, epochs=n_epochs, batch_size=n_batch, verbose=0)
	return model
 
# forecast with a pre-fit model
def model_predict(model, history, config):
	# unpack config
	n_input, _, _, _ = config
	# prepare data
	x_input = np.array(history[-n_input:]).reshape(1, n_input)
	# forecast
	yhat = model.predict(x_input, verbose=0)
	return yhat[0]
 
# walk-forward validation for univariate data
def walk_forward_validation(train, test, cfg):
	predictions = list()

	model = model_fit(train, cfg)
	# seed history with training dataset
	history = [x for x in train]
	# step over each time-step in the test set
	for i in range(len(test)):
		# fit model and make forecast for history
		yhat = model_predict(model, history, cfg)
		# store forecast in list of predictions
		predictions.append(yhat)
		# add actual observation to history for the next loop
		history.append(test[i])
	# estimate prediction error
	error = evaluate(test, predictions)
	return error
 
# repeat evaluation of a config
def repeat_evaluate(df_train_data, df_test_data, config, n_repeats=10):
	# fit and evaluate the model n times
	scores = [walk_forward_validation(df_train_data, df_test_data, config) for _ in range(n_repeats)]
	return scores
 
def multi_layer_perceptron(df_train, df_test, target):

    df_train_series = df_train[target]
    df_test_series = df_test[target]

    df_train_data = df_train_series.values
    df_test_data = df_test_series.values

    # define config
    config = [24, 500, 100, 100]
    # grid search
    scores = repeat_evaluate(df_train_data, df_test_data, config)
    # summarize scores
    final_results = pd.DataFrame.from_dict(scores)
    metrics = pd.DataFrame()
    final_results = final_results.mean()
    metrics = final_results.to_frame().transpose().round(3)
    metrics["target"] = target
    metrics

    return metrics
