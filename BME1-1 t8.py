import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel, chisquare

type_met = ["CpG", "CHG", "CHH"]
type_plant = ["Col-0 FH", "Col-0 AR", "Col-0 GS", "Cvi FH", "Cvi AR", "Cvi GS"]
type_dot = ["ro", "go", "bo"]
type_stage = ["G", "H", "T", "BT", "MG"]
type_gen = ["WT", "dme-2/+"]

data_wt = [0, 0, 0, 3+2+2, 27+23+17+23]
data_dme = [3+1, 17+23+23+25, 1+20+2, 18+1+1+22, 24+1]

print(data_wt, data_dme)

data_nor_wt = [i / sum(data_wt) for i in data_wt]
data_nor_dme = [i / sum(data_dme) for i in data_dme]

print(data_nor_wt, data_nor_dme)

data_exp = [0] * 5
data_exp_wt = [0] * 5
data_exp_dme = [0] * 5

for i in range(5):
    data_exp[i] = data_wt[i] + data_dme[i]

for i in range(5):
    data_exp_wt[i] = data_exp[i] * sum(data_wt)/sum(data_exp)
    data_exp_dme[i] = data_exp[i] * sum(data_dme)/sum(data_exp)

print(data_exp, data_exp_wt, data_exp_dme)

print(sum(data_exp), sum(data_exp_wt), sum(data_exp_dme))
print(chisquare(data_wt, f_exp=data_exp_wt))
print(chisquare(data_dme, f_exp=data_exp_dme))

arr = np.array([data_wt, data_dme])
print(arr)
df = pd.DataFrame(arr)

print(chisquare([0, 97], f_exp=[0.000000001, 97]))
print(chisquare([92, 90], f_exp=[91, 91]))
print(chisquare([91, 91], f_exp=[91, 91]))
