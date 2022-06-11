from neuron import Neuron


class Layer:

	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		assert weight_num > 0 and neurons_num > 0
		self.neurons = []
		self.activation_function = fun
		self.learning_rate = learn_rate
		for i in range(neurons_num):
			self.neurons.append(Neuron(weight_num=weight_num, fun=self.activation_function))

	def values(self, xs):
		t = []
		print(F"Cal value of layer: {self} for values: {xs}")
		for n in self.neurons:
			tmp = n.run(xs)
			print(f"neuron: {tmp}")
			t.append(tmp)

		assert len(t) == len(self.neurons)
		return t


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

	def values(self, xs):
		t = []
		print(F"Cal value of layer: {self} for values: {xs}")
		for n in self.neurons:
			tmp = n.run(xs)
			print(f"neuron: {tmp}")
			t.append(tmp)

		assert len(t) == len(self.neurons)
		return t

class OutputLayer(Layer):
	def __init__(self, neurons_num, weight_num, learn_rate, fun):
		super().__init__(neurons_num, weight_num, learn_rate, fun)

	def __repr__(self):
		return F"<OutputLayer neurons={len(self.neurons)} weights_per_neuron={len(self.neurons[0].weights)}>"

