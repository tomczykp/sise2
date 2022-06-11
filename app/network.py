from layers import HiddenLayer, InputLayer, OutputLayer
from data import ILOSC_PKT
import matplotlib.pyplot as plt
from random import shuffle


class Network:

	def __init__(self, neurons_num, activation_function, io_num=2, rate=0.5, mini_batch_size=8):
		assert io_num > 0 and neurons_num > 0
		self.layers = []
		self.io_num = io_num
		self.learning_rate = rate
		self.mini_batch_size = mini_batch_size
		self.klasy = {}
		self.data = []
		self.fun = activation_function

		self.layers.append(InputLayer(io_num, io_num, rate))
		self.layers.append(HiddenLayer(neurons_num, io_num, rate))
		self.layers.append(OutputLayer(ILOSC_PKT, neurons_num, rate))

	# method when network is already trained
	def oblicz(self, xs):
		netX = [xs]
		for layer in self.layers:
			netX.append(layer.values(netX[-1]))
		return netX

	# # # # # # # # # # # # #
	#   network learning    #
	# # # # # # # # # # # # #
	def train(self, data):
		# data preparation
		data = self.prepare_data(data)
		n = len(data)
		# cut data in batches, for optimization
		mini_batches = [data[k:k + self.mini_batch_size] for k in range(0, n, self.mini_batch_size)]
		for batch in mini_batches:
			self.update_batch(batch)
			return  # DEBUG

	@staticmethod
	def wyznacz_blad(uzyskane, wzorowe):
		suma = 0
		for x, y in zip(uzyskane, wzorowe):
			suma += (x - y) ** 2
		return suma / 2

	def update_batch(self, data):
		blad = []
		for xs in data:  # dla kazdego t z T
			netX = [xs[:-1]]
			zs = []
			for layer in self.layers:
				z = layer.values(netX[-1])
				zs.append(z)
				netX.append(list(map(self.fun, z)))

			blad.append(self.wyznacz_blad(netX[-1], xs[-1]))

	# # # # # # # # # # # # #
	#   data preparation    #
	# # # # # # # # # # # # #
	def wyznacz_klasy(self, data):
		index = 0
		for xs in data:
			key = f"{int(xs[2])}x{int(xs[3])}"
			tmp = self.klasy.get(key)
			if tmp is None:
				self.klasy[key] = index
				index += 1
		assert len(self.klasy) == ILOSC_PKT

	def prepare_data(self, data):
		self.data = data.values.tolist()
		shuffle(self.data)
		self.wyznacz_klasy(self.data)
		return [[xs[0], xs[1], self.target(xs[2], xs[3])] for xs in self.data]

	def target(self, x, y):
		index = self.klasy[f"{int(x)}x{int(y)}"]
		wzorowe = [0] * len(self.klasy)
		wzorowe[index] = 1
		return wzorowe

	# # # # # # # # # # # # #
	#       statistics      #
	# # # # # # # # # # # # #
	def show(self):
		plot(self.data)
		print(self)

	def __repr__(self):
		return f"<NeuralNetwork layers_num={len(self.layers)} layers={self.layers}>"


def plot(data):
	plt.plot(
			list(map(lambda t: t[0], data)),
			list(map(lambda t: t[1], data)), 'b*')
	plt.plot(
			list(map(lambda t: t[2], data)),
			list(map(lambda t: t[3], data)), 'rx')
	plt.title("DANE")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()
