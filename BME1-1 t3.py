import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel

type_met = ["CpG", "CHG", "CHH"]
type_plant = ["Col-0 FH", "Col-0 AR", "Col-0 GS", "Cvi FH", "Cvi AR", "Cvi GS"]
type_dot = ["ro", "go", "bo"]

len_chr = [0, 305, 197, 235, 186, 270]

pos_cen = [0, 150, 36, 137, 39, 117]
k = 100000

met = dict()

met["CpG"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CG")
met["CHG"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CHG")
met["CHH"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CHH")

met_chr = dict()

for tm in type_met:
    met_chr[tm] = list()
    for i in range(6):
        met_chr[tm].append(met[tm].loc[met[tm]["Chr"] == i])

for tm in type_met:
    print(tm)
    print(met[tm][type_plant[0:3]].describe())


comb = [(0, 1), (1, 2), (0, 2), (3, 4), (3, 5), (4, 5), (0, 3), (1, 4), (2, 5)]

arr_test = np.zeros([6, 6])

for tm in type_met:
    for c in comb:
        col0 = met[tm][type_plant[c[0]]]
        col1 = met[tm][type_plant[c[1]]]
        print(tm, type_plant[c[0]], type_plant[c[1]])
        print(ttest_rel(col0, col1))
        arr_test[c[0], c[1]] = ttest_rel(col0, col1)[1]
    print(tm)
    print(arr_test)
