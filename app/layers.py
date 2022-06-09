from neuron import Neuron


class Layer:

	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		assert weight_num > 0 and neurons_num > 0
		self.neurons = []
		self.activation_function = fun
		for i in range(neurons_num):
			self.neurons.append(Neuron(weight_num=weight_num, rate=learn_rate, fun=self.activation_function))


class HiddenLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		super().__init__(neurons_num, weight_num, learn_rate, fun)

	def __repr__(self):
		return F"<HiddenLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"


class InputLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		super().__init__(neurons_num, weight_num, learn_rate, fun)

	def __repr__(self):
		return F"<InputLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"


class OutputLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		super().__init__(neurons_num, weight_num, learn_rate, fun)

	def __repr__(self):
		return F"<OutputLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"

