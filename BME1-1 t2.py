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

met_chr_100k = dict()

for tm in type_met:
    met_chr_100k[tm] = dict()
    for i in range(1, 6):
        met_chr_100k[tm][i] = pd.read_excel("BME1-1_met_chr_100k.xlsx", sheet_name=tm+str(i))

for j in range(1, 6):
    fig, axes = plt.subplots(4, 1, figsize=(len_chr[j] / 25, 7), gridspec_kw={'height_ratios': [1, 6, 6, 6]})
    plt.subplots_adjust(wspace=0, hspace=0.1, left=0, bottom=0, right=1, top=1)

    array_temp = np.zeros((2, len_chr[j]))
    for i in range(int((len_chr[j]-1)/10)+1):
        array_temp[0, i*10] = 50
    array_temp[1, pos_cen[j]] = 100
    array_temp[1, pos_cen[j]+1] = 100
    array_temp[1, pos_cen[j]-1] = 100

    sns.heatmap(array_temp, ax=axes[0], vmax=100, vmin=0,
                xticklabels=False, yticklabels=False,
                cmap="Greys",
                square=False,
                cbar=False)

    for i, tm in enumerate(type_met):
        array_temp = pd.DataFrame(met_chr_100k[tm][j][type_plant]).to_numpy()
        print(array_temp)
        array_temp = array_temp.transpose()

        sns.heatmap(array_temp, ax=axes[i+1], vmax=100, vmin=0,
                    xticklabels=False, yticklabels=False,
                    cmap="coolwarm",
                    square=False,
                    cbar=False)

    plt.show()
