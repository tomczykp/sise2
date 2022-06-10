from layers import HiddenLayer, InputLayer, OutputLayer


class Network:

    def __init__(self, layers_num, neurons_num, activation_function, io_num=2, rate=0.5):
        assert io_num > 0 and neurons_num > 0 and layers_num > 0
        self.layers = []
        self.io_num = io_num
        self.learning_rate = rate

        self.layers.append(InputLayer(io_num, io_num, rate, activation_function))

        self.layers.append(HiddenLayer(neurons_num, io_num, rate, activation_function))
        for i in range(layers_num - 1):
            self.layers.append(HiddenLayer(neurons_num, neurons_num, rate, activation_function))

        self.layers.append(OutputLayer(io_num, neurons_num, rate, activation_function))

    def train(self, data):

        for xs in data.values.tolist():
            value = self.single_run([xs[0], xs[1]])
            blad = self.blad_globalny(value, [xs[2], xs[3]])

    def single_run(self, xs):
        for layer in self.layers:
            xs = layer.values(xs)

        return xs

    def blad_globalny(self, uzyskane, wzorowe):
        suma = 0
        for x, y in zip(uzyskane, wzorowe):
            suma += (x - y)**2
        return self.learning_rate*suma/2

    def show(self):
        print(self)

    def __repr__(self):
        return f"<NeuralNetwork layers_num={len(self.layers)} layers={self.layers}>"
