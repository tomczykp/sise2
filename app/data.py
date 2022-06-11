import pandas as pd


ILOSC_PKT = 225


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


def prepare_data(data):
    data = data.values.tolist()
    wynik = []


    return wynik
