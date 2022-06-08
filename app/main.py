from network import Network
from data import loadTrainData, loadDynamicData, loadRandData


def main():
    d = loadTrainData(8)
    rnd = loadDynamicData(8)
    net = Network(data=d, layers=2, neurons=20, hidNeurons=10)
    net.train()
    net.show()


if __name__ == '__main__':
   main()

