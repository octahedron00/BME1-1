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

met_chr_100k = dict()

for tm in type_met:
    met_chr_100k[tm] = dict()
    for i, lc in enumerate(len_chr):
        met_chr_100k[tm][i] = pd.DataFrame(columns=["End"] + type_plant)
        for j in range(lc):
            dic_temp = {"End": j * k + k}
            for tp in type_plant:
                df_temp = pd.DataFrame(met_chr[tm][i]).loc[
                    (j * k < met_chr[tm][i]["End"]) & (met_chr[tm][i]["End"] <= j * k + k)]
                # print(df_temp)
                mean_temp = df_temp[tp].mean()
                dic_temp[tp] = mean_temp
            met_chr_100k[tm][i] = pd.concat([met_chr_100k[tm][i], pd.DataFrame(dic_temp, index=[j])], ignore_index=True)
        # print(tm, i, met_chr_100k[tm][i])

for i in range(1, 6):
    for j, tm in enumerate(type_met):
        plt.subplot(3, 5, j * 5 + i)
        for k, tp in enumerate(type_plant[0:3]):
            plt.plot(met_chr_100k[tm][i]["End"], met_chr_100k[tm][i][tp], type_dot[k], markersize=1)

print("plt_show")
plt.show()

with pd.ExcelWriter("BME1-1_met_chr_100k.xlsx") as writer:
    for i in range(1, 6):
        for j, tm in enumerate(type_met):
            met_chr_100k[tm][i].to_excel(writer, sheet_name=tm+str(i))
