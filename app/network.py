from layers import HiddenLayer, InputLayer, OutputLayer


class Network:

    def __init__(self, layers_num, neurons_num, activation_function, io_num=2, rate=0.5):
        assert io_num > 0 and neurons_num > 0 and layers_num > 0
        self.layers = []

        self.layers.append(InputLayer(io_num, 1, rate, activation_function))

        self.layers.append(HiddenLayer(neurons_num, io_num, rate, activation_function))
        for i in range(layers_num - 1):
            self.layers.append(HiddenLayer(neurons_num, neurons_num, rate, activation_function))

        self.layers.append(OutputLayer(io_num, neurons_num, rate, activation_function))

    def train(self, data):
        pass

    def show(self):
        print(self)

    def __repr__(self):
        return f"<NeuralNetwork layers_num={len(self.layers)} layers={self.layers}>"
