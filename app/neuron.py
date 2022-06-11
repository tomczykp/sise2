from random import uniform


class Neuron:

	def __init__(self, weight_num):
		self.weights = []
		for x in range(weight_num + 1):
			self.weights.append(uniform(-0.5, 0.5))

	def run(self, xs):
		suma = 0
		for x, w in zip(xs, self.weights):
			suma += x*w

		return suma + self.weights[-1]

	def update(self, xs):
		pass

	def __repr__(self):
		return f"<Neuron weights={self.weights}>"
