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


def prepare_data():
	if path.isfile(f"x_{filename}"):
		with open(f"x_{filename}", 'r') as file_object:
			x_train = load(file_object)
		with open(f"y_{filename}", 'r') as file_object:
			y_train = load(file_object)
		return x_train, y_train

	print("DATA NOT IMPORTED .... LOADING FROM ORIGINAL FILES")
	data = loadTrainData(8)
	shuffle(data)
	wyznacz_klasy(data)
	x_train, y_train = [], []
	for xs in data:
		if isnan(xs[0]) or isnan(xs[1]) or isnan(xs[2]) or isnan(xs[3]):
			continue
		x_train.append([xs[0], xs[1]])
		y_train.append(target(xs[2], xs[3]))

	with open(f"x_{filename}", 'w') as file_object:
		dump(x_train, file_object)
	with open(f"y_{filename}", 'w') as file_object:
		dump(y_train, file_object)
	return x_train, y_train


def target(x, y):
	return klasy[f"{int(x)}x{int(y)}"]
