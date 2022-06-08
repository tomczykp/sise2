class Network:

    def __init__(self, data, layers, neurons, hidNeurons):
        self.data = data
        self.layers_num = layers
        self.in_neu_num = neurons
        self.hid_neu_num = hidNeurons

    def train(self):
        print(f"Data: {self.data}")

    def show(self):
        print(self)

    def __repr__(self):
        return f"<NeuralNetwork data={len(self.data)}, layers={self.layers_num}>"
