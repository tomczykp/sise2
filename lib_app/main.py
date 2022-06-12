import tensorflow as tf
from data_preparation import prepare_data, plot
import numpy as np
from plot import PlotLearning, plot_loss


def error_fun(x, y):
	return (x[0] - y[0])**2 + (x[1] - y[1])**2


def main():

	xs, ys = prepare_data()
	n = len(xs)
	index = int(2*n/3)
	x_train, x_test = xs[:index], xs[index:]
	y_train, y_test = ys[:index], ys[index:]

	x_train = np.asarray(x_train)
	y_train = np.asarray(y_train)

	assert not np.any(np.isnan(ys))
	for x in xs:
		assert not np.any(np.isnan(x))

	model = tf.keras.models.Sequential([
		tf.keras.layers.Dense(4),
		tf.keras.layers.Dense(8, activation='sigmoid'),
		tf.keras.layers.Dense(2)
	])

	callbacks_list = [PlotLearning()]
	loss_fn = tf.keras.losses.MeanSquaredError()
	opt = tf.keras.optimizers.SGD(learning_rate=0.08)

	model.compile(optimizer=opt, loss=loss_fn, metrics=['accuracy'])

	history = model.fit(x_train, y_train, epochs=2, callbacks=callbacks_list, validation_data=(x_test, y_test))
	model.evaluate(x_test, y_test, verbose=2)
	vals = model.predict(x_train)
	plot(vals, x_train)
	plot_loss(history)
	print(model.trainable_variables)

	err_raw = calc_density([error_fun(x,y) for x, y in zip(x_train, y_train)])
	err_refined = calc_density([error_fun(x,y) for x, y in zip(vals, y_train)])

	plot(err_raw, err_refined)


def calc_density(errs):
	errs_denisty = {}
	for err in errs:
		err = round(err, 4)
		if errs_denisty.get(err) is None:
			errs_denisty[err] = 0
		errs_denisty[err] += 1
	return list(map(lambda xi: (xi[1], xi[0]), list(errs_denisty.items())))


if __name__ == '__main__':
	main()

