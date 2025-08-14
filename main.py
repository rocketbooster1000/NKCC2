import numpy as np
import pandas as pd
from matplotlib import pyplot
import os

if not os.path.exists("E"):
    os.mkdir("E")

if not os.path.exists("F"):
    os.mkdir("F")
# pdb_identifier = "D 0730"
# file_path = ""
# mpnn_results_file = open(file_path + "mpnnresults.csv", "r")

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [3, 7, 4, 2, 1, 4, 2, 3, 5]
x2 = [3, 2, 6, 1, 3, 6, 8, 0, 2, 2]
y2 = [9, 5, 2, 7, 3, 7, 3, 7, 3, 7]

design_0_df = pd.concat([pd.read_csv("E F/0mpnn_results.csv", nrows=16), pd.read_csv("E F/1mpnn_results.csv", nrows=16), pd.read_csv("E F/2mpnn_results.csv", nrows=16)], ignore_index=True)
ax1 = design_0_df.plot.scatter(x="plddt", y="rmsd")
ax1.set_title("E: Design 0")
print(design_0_df)
pyplot.savefig("E/E_Design_0.png")
design_0_df.to_csv("E/E-master.csv", index = False)

# design_1_df = pd.read_csv("E F/0mpnn_results.csv", skiprows=[x for x in range(1, 17)])
design_1_df = pd.concat([pd.read_csv("E F/0mpnn_results.csv", skiprows=[x for x in range(1, 17)]), pd.read_csv("E F/1mpnn_results.csv", skiprows=[x for x in range(1, 17)]), pd.read_csv("E F/2mpnn_results.csv", skiprows=[x for x in range(1, 17)])], ignore_index=True)
ax2 = design_1_df.plot.scatter(x="plddt", y="rmsd")
ax2.set_title("F: Design 1")
pyplot.savefig("F/F_Design_1.png")
print("-------")
print(design_1_df)
design_1_df.to_csv("F/F-master.csv", index = False)
pyplot.show()
# pyplot.scatter(x2, y2)
# pyplot.xlabel("x")
# pyplot.ylabel("y")
# pyplot.show()


