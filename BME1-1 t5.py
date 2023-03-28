import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel

# For the processing of TAIR10 Data

type_met = ["CpG", "CHG", "CHH"]
type_plant = ["Col-0 FH", "Col-0 AR", "Col-0 GS", "Cvi FH", "Cvi AR", "Cvi GS"]
type_dot = ["ro", "go", "bo"]
not_list_before = ["gene", "transposable_element"]
not_list = ["gene", "promoter", "transposable_element"]

len_chr = [0, 305, 197, 235, 186, 270]
k = 100000

m = 50 / 2

met = dict()

met["CpG"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CG")
met["CHG"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CHG")
met["CHH"] = pd.read_excel("BME1-1_Data.xlsx", sheet_name="CHH")

met_chr = dict()

for tm in type_met:
    met_chr[tm] = list()
    for i in range(6):
        met_chr[tm].append(met[tm].loc[met[tm]["Chr"] == i])

pos_not = [dict()]

for i in range(1, 6):
    pos_not.append(dict())
    for no in not_list_before:
        pos_not[i][no] = pd.read_excel("BME1-1_Notation.xlsx", sheet_name=no + str(i))

for tm in type_met:
    for i in range(1, 6):

        p_ge = 0  # gene sheet position
        p_te = 0  # transposable sheet element(TE) position
        for no in not_list:
            met_chr[tm][i].insert(0, no, False)
        for index, row in met_chr[tm][i].iterrows():
            pos = row["End"] - m

            while True:
                if pos_not[i]["gene"].shape[0] <= p_ge:
                    break
                if pos <= pos_not[i]["gene"].iloc[p_ge]["End"]:
                    break
                p_ge += 1

            if pos_not[i]["gene"].shape[0] > p_ge:
                if pos_not[i]["gene"].iloc[p_ge]["Start"] < pos < pos_not[i]["gene"].iloc[p_ge]["End"]:
                    met_chr[tm][i].loc[index, "gene"] = True

            while True:
                if pos_not[i]["gene"].shape[0] <= p_ge:
                    break
                if pos <= pos_not[i]["gene"].iloc[p_ge]["Start"]:
                    break
                p_ge += 1

            if pos_not[i]["gene"].shape[0] > p_ge:
                if pos_not[i]["gene"].iloc[p_ge]["Start"]-1000 < pos <= pos_not[i]["gene"].iloc[p_ge]["Start"]:
                    met_chr[tm][i].loc[index, "promoter"] = True

            while True:
                if pos_not[i]["transposable_element"].shape[0] <= p_te:
                    break
                if pos <= pos_not[i]["transposable_element"].iloc[p_te]["End"]:
                    break
                p_te += 1

            if pos_not[i]["transposable_element"].shape[0] > p_te:
                if pos_not[i]["transposable_element"].iloc[p_te]["Start"] < pos < pos_not[i]["transposable_element"].iloc[p_te]["End"]:
                    met_chr[tm][i].loc[index, "transposable_element"] = True

        print(tm, i)
        print("total   ", met_chr[tm][i].shape[0])
        print("gene    ", met_chr[tm][i].loc[met_chr[tm][i]["gene"] == True].shape[0])
        print("promoter", met_chr[tm][i].loc[met_chr[tm][i]["promoter"] == True].shape[0])
        print("TEs     ", met_chr[tm][i].loc[met_chr[tm][i]["transposable_element"] == True].shape[0])


with pd.ExcelWriter("BME1-1_met_chr_not.xlsx") as writer:
    for i in range(1, 6):
        for tm in type_met:
            met_chr[tm][i].to_excel(writer, sheet_name=tm+str(i))

