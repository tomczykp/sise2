from data import loadTrainData, ILOSC_PKT
from Network import Network


def main():
    #     d = loadTrainData(8)
    #     f = lambda x: 1 / (1 + exp(-x))
    #     net = Network(layers_num=2, neurons_num=20, io_num=2, rate=0.5, activation_function=f)
    #     net.train(d)
    #     net.show()
    net = Network([2, 20, 20, ILOSC_PKT])
    d = loadTrainData(8)
    net.feedforward(d)


if __name__ == '__main__':
    main()
