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
not_list = ["gene", "transposable_element"]

len_chr = [0, 305, 197, 235, 186, 270]
k = 100000


pos = pd.read_excel("BME1-1_TAIR10_GFF3.xlsx")
print(pos)

pos_not = list()

for i in range(6):
    pos_not.append(dict())
    for no in not_list:
        pos_not[i][no] = pos.loc[(pos["Type"] == no) & (pos["Chr"] == "Chr"+str(i))]

with pd.ExcelWriter("BME1-1_Notation.xlsx") as writer:
    for i in range(1, 6):
        for no in not_list:
            pos_not[i][no].to_excel(writer, sheet_name=no+str(i))

