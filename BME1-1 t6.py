import math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel, ttest_ind

# For the processing of TAIR10 Data

type_met = ["CpG", "CHG", "CHH"]
type_plant = ["Col-0 FH", "Col-0 AR", "Col-0 GS", "Cvi FH", "Cvi AR", "Cvi GS"]
type_stage = ["FH", "AR", "GS"]
type_ecotype = ["Col-0", "Cvi"]
type_dot = ["ro", "go", "bo"]
type_not = ["total", "gene", "promoter", "transposable_element", "etc."]

len_chr = [0, 305, 197, 235, 186, 270]
k = 100000

m = 50 / 2

met_chr = dict()

for tm in type_met:
    met_chr[tm] = [0, 0, 0, 0, 0, 0]
    for i in range(1, 6):
        met_chr[tm][i] = pd.read_excel("BME1-1_met_chr_not.xlsx", sheet_name=tm+str(i))

met = dict()
for tm in type_met:
    met[tm] = pd.concat([met_chr[tm][i] for i in range(1, 6)])
    print(met[tm])

met_t = dict()
for tn in type_not:
    met_t[tn] = dict()

for tm in type_met:
    met_t[type_not[0]][tm] = met[tm]
    met_t[type_not[1]][tm] = met[tm].loc[met[tm]["gene"] == True]
    met_t[type_not[2]][tm] = met[tm].loc[met[tm]["promoter"] == True]
    met_t[type_not[3]][tm] = met[tm].loc[met[tm]["transposable_element"] == True]
    met_t[type_not[4]][tm] = met[tm].loc[(met[tm]["gene"] == False) & (met[tm]["promoter"] == False) & (met[tm]["transposable_element"] == False)]

mean_tt = dict()

for tn in type_not:
    mean_tt[tn] = dict()
    for tm in type_met:
        print(tn, tm)
        print(met_t[tn][tm].shape[0])
        print(met_t[tn][tm][type_plant].mean())
        mean_tt[tn][tm] = met_t[tn][tm][type_plant].mean()

pvalue_tt = dict()

comb = [(0, 1), (1, 2), (0, 2), (3, 4), (3, 5), (4, 5), (0, 3), (1, 4), (2, 5)]

for tn in type_not:
    pvalue_tt[tn] = dict()
    for tm in type_met:
        arr_test = np.zeros([6, 6])
        for c in comb:
            col0 = met_t[tn][tm][type_plant[c[0]]]
            col1 = met_t[tn][tm][type_plant[c[1]]]
            arr_test[c[0], c[1]] = ttest_rel(col0, col1)[1]
            print(tn, tm, type_plant[c[0]], type_plant[c[1]], ttest_rel(col0, col1)[1] < 0.05, ttest_rel(col0, col1)[1])
        pvalue_tt[tn][tm] = arr_test


print("START1")
for tn1 in type_not:
    for tn2 in type_not:
        for tm in type_met:
            for tp in type_plant:
                if tn1 != tn2:
                    print(ttest_ind(met_t[tn1][tm][tp], met_t[tn2][tm][tp])[1] < 0.05, tn1, tn2, tm, tp)
print("END1")

print("START2")
for tn in type_not:
    for tm1 in type_met:
        for tm2 in type_met:
            for tp in type_plant:
                if tm1 != tm2:
                    print(ttest_ind(met_t[tn][tm1][tp], met_t[tn][tm2][tp])[1] < 0.05, tn, tm1, tm2, tp)
print("END2")



fig, axes = plt.subplots(5, 3, figsize=(20, 20))
plt.subplots_adjust(wspace=0.2, hspace=0.25, left=0.05, bottom=0.05, right=0.95, top=0.98)
for b, tm in enumerate(type_met):
    for a, tn in enumerate(type_not):
        ax = axes[a][b]
        tnn = tn
        if tn == type_not[3]:
            tnn = "TE"
        ax.set_title(tm + " methylation level of " + tnn + " region (n=" + str(met_t[tn][tm].shape[0]) + ")")
        x = np.arange(3)
        label = ["", "", "", "", "", ""]
        for i in range(2):
            v = np.zeros(shape=3)
            for j in range(3):
                v[j] = mean_tt[tn][tm][type_plant[i*3 + j]]
            for j in range(3):
                label[i*3+j] = str(round(v[j], 2))
                if i == 0:
                    if pvalue_tt[tn][tm][j, j+3] < 0.05:
                        label[j] = "**\n" + label[j]
            if (pvalue_tt[tn][tm][i*3, i*3+1] < 0.05) & (pvalue_tt[tn][tm][i*3+1, i*3+2] < 0.05):
                label[i*3+1] = "*\n" + label[i*3+1]
            if (pvalue_tt[tn][tm][i*3, i*3+1] < 0.05) & (pvalue_tt[tn][tm][i*3, i*3+2] < 0.05):
                label[i*3] = "*\n" + label[i*3]
            if (pvalue_tt[tn][tm][i*3, i*3+2] < 0.05) & (pvalue_tt[tn][tm][i*3+1, i*3+2] < 0.05):
                label[i*3+2] = "*\n" + label[i*3+2]
            ax.bar(x + (i * 0.25 - 0.125), v, 0.25)
        for n, patch in enumerate(ax.patches):
            ax.text(patch.get_x()+0.125, patch.get_height() + ax.get_ylim()[1]*0.02,
                     label[n], fontsize=10, ha="center")
        ax.set_xticks(x, type_stage)
        ax.legend(type_ecotype, loc="lower right")

        ax.set_ylim([0, ax.get_ylim()[1]*1.15])

        ax.set_xlabel("Stage of the seed")
        ax.set_ylabel("% methylation")
plt.savefig("Total.png")

