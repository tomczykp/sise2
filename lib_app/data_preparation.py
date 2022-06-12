from random import shuffle
import pandas as pd
from numpy import isnan, min, max
from json import load, dump
from os import path
import matplotlib.pyplot as plt


ILOSC_PKT = 225
filename = "dane"


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


def normalize_data(data):
	return (data - min(data)) / (max(data) - min(data))


def prepare_data():
	nr_sali = 10
	if path.isfile(f"x_{filename}{nr_sali}.json"):
		with open(f"x_{filename}{nr_sali}.json", 'r') as file_object:
			x_train = load(file_object)
		with open(f"y_{filename}{nr_sali}.json", 'r') as file_object:
			y_train = load(file_object)
		return x_train, y_train

	print("DATA NOT IMPORTED .... LOADING FROM ORIGINAL FILES")
	data = loadTrainData(nr_sali)
	shuffle(data)
	x_train, y_train = [], []
	xs, ys = [], []
	xsW, ysW = [], []
	for t in data:
		if isnan(t[0]) or isnan(t[1]) or isnan(t[2]) or isnan(t[3]):
			continue
		xs.append(t[0])
		ys.append(t[1])
		xsW.append(t[2])
		ysW.append(t[3])

	for x, y in zip(normalize_data(xs), normalize_data(ys)):
		x_train.append([x, y])

	for x, y in zip(normalize_data(xsW), normalize_data(ysW)):
		y_train.append([x, y])

	with open(f"x_{filename}{nr_sali}.json", 'w') as file_object:
		dump(x_train, file_object)
	with open(f"y_{filename}{nr_sali}.json", 'w') as file_object:
		dump(y_train, file_object)

	return x_train, y_train


def plot(data1, data2=[]):
	plt.plot(
			list(map(lambda t: t[0], data1)),
			list(map(lambda t: t[1], data1)), 'b.')
	plt.plot(
			list(map(lambda t: t[0], data2)),
			list(map(lambda t: t[1], data2)), 'r.')
	plt.title("")
	plt.xlabel("Ilość wystąpień")
	plt.ylabel("Wartość błędu")
	plt.show()