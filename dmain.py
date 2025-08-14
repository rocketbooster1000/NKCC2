import os
import pandas as pd
from matplotlib import pyplot as plt

df = pd.concat([pd.read_csv("D/0mpnn_results.csv"), pd.read_csv("D/1mpnn_results.csv"), pd.read_csv("D/1ompnn_results.csv"), pd.read_csv("D/2mpnn_results.csv"), pd.read_csv("D/ompnn_results.csv")], ignore_index=True)
df.to_csv('D/D-master.csv', index=False)

df.plot.scatter(x="plddt", y="rmsd")
plt.title("D: Design 0")
plt.savefig("D/D_Design_0.png")
plt.show()