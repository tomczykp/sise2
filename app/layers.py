from neuron import Neuron


class Layer:

	def __init__(self, neurons_num, weight_num, learn_rate):
		assert weight_num > 0 and neurons_num > 0
		self.neurons = []
		self.learning_rate = learn_rate
		for i in range(neurons_num):
			self.neurons.append(Neuron(weight_num=weight_num))

	def values(self, xs):
		t = []
		for n in self.neurons:
			tmp = n.run(xs)
			t.append(tmp)
		assert len(t) == len(self.neurons)
		return t


class HiddenLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate):
		super().__init__(neurons_num, weight_num, learn_rate)

	def __repr__(self):
		return F"<HiddenLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"


class InputLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate):
		super().__init__(neurons_num, weight_num, learn_rate)

	def __repr__(self):
		return F"<InputLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"

	def values(self, xs):
		return xs


class OutputLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate):
		super().__init__(neurons_num, weight_num, learn_rate)

	def __repr__(self):
		return F"<OutputLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"

