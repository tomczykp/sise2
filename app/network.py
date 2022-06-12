from layers import HiddenLayer, InputLayer, OutputLayer
from data import ILOSC_PKT
import matplotlib.pyplot as plt
from random import shuffle
import numpy as np


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
	#       statistics      #
	# # # # # # # # # # # # #
	def show(self):
		print(self)

	def __repr__(self):
		return f"<NeuralNetwork layers_num={len(self.layers)} layers={self.layers}>"
