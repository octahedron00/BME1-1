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


fig, ax = plt.subplots()
ax.set_title("Seeds on the development stage")
x = np.arange(5)

plt.bar(x - 0.125, data_wt, 0.25)
plt.bar(x + 0.125, data_dme, 0.25)

label = data_wt+data_dme

for n, patch in enumerate(ax.patches):
    plt.text(patch.get_x()+0.125, patch.get_height() + plt.ylim()[1]*0.02,
             label[n], fontsize=10, ha="center")
plt.xticks(x, type_stage)
plt.legend(type_gen, loc="upper left")

plt.ylim([0, plt.ylim()[1]*1.05])

plt.xlabel("Stage of the seed")
plt.ylabel("# of seed")
plt.show()


fig, ax = plt.subplots()
ax.set_title("Proportion of the seeds on the development stage")
x = np.arange(5)

plt.bar(x - 0.125, data_nor_wt, 0.25)
plt.bar(x + 0.125, data_nor_dme, 0.25)

label = [round(i, 2) for i in (data_nor_wt+data_nor_dme)]

for n, patch in enumerate(ax.patches):
    plt.text(patch.get_x()+0.125, patch.get_height() + plt.ylim()[1]*0.02,
             label[n], fontsize=10, ha="center")
plt.xticks(x, type_stage)
plt.legend(type_gen, loc="upper left")

plt.ylim([0, plt.ylim()[1]*1.05])

plt.xlabel("Stage of the seed")
plt.ylabel("proportion of seed")
plt.show()

