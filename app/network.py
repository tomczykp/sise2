from layers import HiddenLayer, InputLayer, OutputLayer
import matplotlib.pyplot as plt
from data import ILOSC_PKT


def plot(data):
    print(data)
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


class Network:

    def __init__(self, layers_num, neurons_num, activation_function, io_num=2, rate=0.5):
        assert io_num > 0 and neurons_num > 0 and layers_num > 0
        self.layers = []
        self.io_num = io_num
        self.learning_rate = rate
        self.klasy = {}

        self.layers.append(InputLayer(io_num, io_num, rate, activation_function))

        self.layers.append(HiddenLayer(neurons_num, io_num, rate, activation_function))
        for i in range(layers_num - 1):
            self.layers.append(HiddenLayer(neurons_num, neurons_num, rate, activation_function))

        self.layers.append(OutputLayer(ILOSC_PKT, neurons_num, rate, activation_function))

    def train(self, data):
        data = data.values.tolist()
        for x in data:
            print(x)
        return 1

        self.wyznacz_klasy(data)
        data = [[xs[0], xs[1], ] for xs in data]
        print(self.klasy)
        print(len(self.klasy))
        return 1
        values, blad = [], []

        for xs in data:  # dla kazdego t z T
            netX = [xs[:-1]]
            for layer in self.layers:
                netX.append(layer.values(netX[-1]))

            blad.append(self.wyznacz_blad(values[-1], xs[-1]))

    def wyznacz_klasy(self, data):
        index = 0
        for xs in data:
            key = f"{int(xs[2])}x{int(xs[3])}"
            tmp = self.klasy.get(key)
            if tmp is None:
                self.klasy[key] = index
                index += 1.0

    def wyznacz_blad(self, uzyskane, wzorowe):
        suma = 0
        for x, y in zip(uzyskane, wzorowe):
            suma += (x - y)**2
        return suma/2

    def show(self):
        print(self)

    def __repr__(self):
        return f"<NeuralNetwork layers_num={len(self.layers)} layers={self.layers}>"
