from random import shuffle
import pandas as pd
from numpy import isnan
from json import load, dump
from os import path

ILOSC_PKT = 225
filename = "dane.json"


def loadTrainData(sala_nr):
	return loadData("_stat", sala_nr, ILOSC_PKT)


def loadDynamicData(sala_nr):
	t1 = loadData("", sala_nr, 3, "p")
	t2 = loadData("", sala_nr, 3, "z")
	return t1 + t2


def loadRandData(sala_nr):
	return loadData("_random", sala_nr, 2, "p")


def loadData(interfix, sala_nr, end, postfix=""):
	df = pd.DataFrame()
	folder = f"../pomiary/F{sala_nr}"

	for i in range(1, end + 1, 1):
		path = f"{folder}/f{sala_nr}{interfix}_{i}{postfix}.xlsx"
		t1 = pd.read_excel(io=path)

		df = pd.concat([df, t1])
	data = [[x, y, ex, ey] for x, y, ex, ey in
									zip(df['data__coordinates__x'], df['data__coordinates__y'], df['reference__x'], df['reference__y'])]
	return data


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


def prepare_data(sala_nr):
	if path.isfile(f"{filename}"):
		with open(f"{filename}", 'r') as file_object:
			wynik = load(file_object)
		return wynik

	print("DATA NOT IMPORTED .... LOADING FROM ORIGINAL FILES")
	data = loadTrainData(sala_nr)
	shuffle(data)
	wyznacz_klasy(data)
	wynik = []
	for xs in data:
		if isnan(xs[0]) or isnan(xs[1]) or isnan(xs[2]) or isnan(xs[3]):
			continue
		wynik.append([xs[0], xs[1], target(xs[2], xs[3])])

	with open(f"{filename}", 'w') as file_object:
		dump(wynik, file_object)
	return wynik


def target(x, y):
	index = klasy[f"{int(x)}x{int(y)}"]
	wzorowe = [0] * len(klasy)
	wzorowe[index] = 1
	return wzorowe



def plot(data):
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

	
