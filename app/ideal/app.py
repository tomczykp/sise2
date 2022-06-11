from ideal import Network
from data_prepare import prepare_data
from data import loadTrainData, ILOSC_PKT

def main():
    d = loadTrainData(8)
    data = prepare_data(d)
    net = Network([2, 10, 10, ILOSC_PKT])
    net.SGD(data, 2, 8, 0.6)



if __name__ == '__main__':
    main()
