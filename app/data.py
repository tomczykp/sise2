import pandas as pd
import matplotlib.pyplot as plt

ILOSC_PKT = 1


def loadTrainData(sala_nr):
    return loadData("_stat", sala_nr, ILOSC_PKT, "AG,AH,AJ,AK")


def loadDynamicData(sala_nr):
    t1 = loadData("", sala_nr, 3, "AG,AH,AJ,AK", "p")
    t2 = loadData("", sala_nr, 3, "AG,AH,AJ,AK", "z")
    return pd.concat([t1, t2])


def loadRandData(sala_nr):
    return loadData("_random", sala_nr, 2, "B,C,D,E", "p")


def loadData(interfix, sala_nr, end, cols, postfix=""):
    data = pd.DataFrame()
    folder = f"pomiary/F{sala_nr}"

    for i in range(1, end + 1, 1):
        path = f"{folder}/f{sala_nr}{interfix}_{i}{postfix}.xlsx"
        t1 = pd.read_excel(io=path, usecols=cols)

        data = pd.concat([data, t1])

    return data


def wzorowa(index, klasy):
    wzorowe = [0] * len(klasy)
    wzorowe[index] = 1
    return wzorowe


def prepare_data(data):
    data = data.values.tolist()
    klasy = wyznacz_klasy(data)
    train_data, test_data = [], []
    for t in data:
        index = f"{int(t[2])}x{int(t[3])}"
        train_data.append( ((t[0], t[1]), wzorowa(klasy[index], klasy)) )

    return train_data


def wyznacz_klasy(data):
    klasy = {}
    index = 0
    for xs in data:
        key = f"{int(xs[2])}x{int(xs[3])}"
        tmp = klasy.get(key)
        if tmp is None:
            klasy[key] = index
            index += 1
    return klasy


def plot(data1, data2):
    plt.plot(
            list(map(lambda t: t[0], data1)),
            list(map(lambda t: t[1], data1)), 'b*')
    plt.plot(
            list(map(lambda t: t[0], data2)),
            list(map(lambda t: t[1], data2)), 'rx')
    plt.title("DANE")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def plot_four(data):
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

