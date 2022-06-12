from tensorflow import keras
from matplotlib import pyplot as plt


class PlotLearning(keras.callbacks.Callback):
	"""
	Callback to plot the learning curves of the model during training.
	"""

	def on_train_begin(self, logs={}):
		self.metrics = {}
		for metric in logs:
			self.metrics[metric] = []

	def on_epoch_end(self, epoch, logs={}):
		# Storing metrics
		for metric in logs:
			if metric in self.metrics:
				self.metrics[metric].append(logs.get(metric))
			else:
				self.metrics[metric] = [logs.get(metric)]

		# Plotting
		metrics = [x for x in logs if 'val' not in x]

		f, axs = plt.subplots(1, len(metrics), figsize=(15, 5))

		for i, metric in enumerate(metrics):
			axs[i].plot(range(1, epoch + 2),
						self.metrics[metric],
						label=metric)

			# if logs['val_' + metric]:
			# 	axs[i].plot(range(1, epoch + 2),
			# 				self.metrics['val_' + metric],
			# 				label='val_' + metric)

			axs[i].legend()
			axs[i].grid()

		plt.tight_layout()
		plt.show()



def plot_loss(history):

	# Get training and test loss histories
	training_loss = history.history['loss']
	test_loss = history.history['val_loss']

	# Create count of the number of epochs
	epoch_count = range(1, len(training_loss) + 1)

	# Visualize loss history
	plt.plot(epoch_count, training_loss, 'r--')
	plt.plot(epoch_count, test_loss, 'b-')
	plt.legend(['Training Loss', 'Test Loss'])
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.show()

