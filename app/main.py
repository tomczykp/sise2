from data import prepare_data
from network import Network, plot
from numpy import exp


def main():
	d = prepare_data(8)
	f = lambda x: 1 / (1 + exp(-x))
	net = Network(neurons_num=20, io_num=2, rate=0.5, activation_function=f, mini_batch_size=8)
	net.train(d)
	net.show()


if __name__ == '__main__':
	main()
