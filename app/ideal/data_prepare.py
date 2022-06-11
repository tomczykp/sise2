from data import ILOSC_PKT
from random import shuffle
from numpy import asarray


klasy = {}
def wyznacz_klasy(data):
	index = 0
	for xs in data:
		key = f"{int(xs[2])}x{int(xs[3])}"
		tmp = klasy.get(key)
		if tmp is None:
			klasy[key] = index
			index += 1
	assert len(klasy) == ILOSC_PKT

def prepare_data(data):
	data = data.values.tolist()
	shuffle(data)
	wyznacz_klasy(data)
	return [[ asarray((xs[0], xs[1])), asarray(target(xs[2], xs[3]))] for xs in data]

def target(x, y):
	index = klasy[f"{int(x)}x{int(y)}"]
	wzorowe = [0] * len(klasy)
	wzorowe[index] = 1
	return wzorowe
