from data import loadTrainData
from network import Network
from numpy import exp


def main():
    d = loadTrainData(8)
    f = lambda x: 1 / (1 + exp(-x))
    net = Network(layers_num=2, neurons_num=20, io_num=2, rate=0.5, activation_function=f)
    net.train(d)
    net.show()


if __name__ == '__main__':
    main()
