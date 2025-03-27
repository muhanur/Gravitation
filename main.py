import warnings
import sys
warnings.filterwarnings('ignore')

import numpy as np, pandas as pd
from numpy import inf

Oi = np.round(pd.read_excel('./data/supply.xlsx').T.values[0], decimals=4)
Dj = pd.read_excel('./data/demand.xlsx').T.values[0]
W_data = pd.read_excel('./data/weight.xlsx').to_numpy()

filepath = "./data/result_15.csv"
i = 1

# Write file
def write_file(filepath, data):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)

# Create first temp data
W_temp = (Dj * Oi[np.newaxis].T) / W_data
W_temp[W_temp == inf] = 0 #Change inf to 0
type = 1
num_of_iteration = 100000

while i < num_of_iteration:
    print("Iteration {}".format(i + 1))
    if type == 0:
        Dd = W_temp.sum(axis=type)
        if (Dd==Dj).all() == False:
            Bj = Dj / Dd
            W_temp = W_temp * Bj
            type = 1
        else:
            write_file(filepath, W_temp)
            print("Iteration Finish")
            break
    else:
        Dd = W_temp.sum(axis=type)
        if (Dd==Oi).all() == False:
            Ai = Oi / Dd
            W_temp = W_temp * Ai[np.newaxis].T
            type = 0
        else:
            write_file(filepath, W_temp)
            print("Iteration Finish")
            break

    i += 1

    if i == num_of_iteration:
        write_file(filepath, W_temp)