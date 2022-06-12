import tensorflow as tf
from data_preparation import prepare_data, ILOSC_PKT
import numpy as np


def main():

	xs, ys = prepare_data()
	n = len(xs)
	index = int(2*n/3)
	x_train, x_test = xs[:index], xs[index:]
	y_train, y_test = ys[:index], ys[index:]

	assert not np.any(np.isnan(ys))
	for x in xs:
		assert not np.any(np.isnan(x))

	model = tf.keras.models.Sequential([
		tf.keras.layers.Dense(220, activation='selu'),
		tf.keras.layers.Dense(140, activation='selu'),
		tf.keras.layers.Dense(460, activation='selu'),
		tf.keras.layers.Dense(ILOSC_PKT)
	])

	loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
	opt = tf.keras.optimizers.Nadam(learning_rate=0.0012)

	model.compile(optimizer=opt, loss=loss_fn, metrics=['accuracy'])

	model.fit(x_train, y_train, epochs=40)
	model.evaluate(x_test, y_test, verbose=2)


if __name__ == '__main__':
	main()

