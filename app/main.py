from network import Network
from data import loadTrainData, loadDynamicData, loadRandData


def main():
    d = loadTrainData(8)
    rnd = loadDynamicData(8)
    net = Network(layers_num=2, neurons_num=20, io_num=2, rate=0.5, activation_function=lambda x: x)
    net.train(d)
    net.show()


if __name__ == '__main__':
   main()

