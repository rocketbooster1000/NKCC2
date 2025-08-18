import os
import pandas as pd
from matplotlib import pyplot as plt

plddt_threshold = 0.7
rmsd_threshold = 5

if not os.path.exists("D/Plots"):
    os.makedirs("D/Plots")
    
if os.path.exists("D/D-master.csv"):
    os.remove("D/D-master.csv")
    
pd_files = []

for filename in os.listdir("D/temp0.3"):
    if (filename.endswith(".csv")):
        pd_files.append(pd.read_csv(os.path.join("D/temp0.3", filename)))

df = pd.concat(pd_files, ignore_index=True)
df.to_csv('D/D-master.csv', index=False)

print(df.describe())
if os.path.exists("D/D-filtered.csv"):
    os.remove("D/D-filtered.csv")
df[(df['plddt'] > plddt_threshold) & (df['rmsd'] < rmsd_threshold)].to_csv("D/D-filtered.csv", index=False)

mask = (df['plddt'] > plddt_threshold) & (df['rmsd'] < rmsd_threshold)
plt.scatter(df[mask]['plddt'], df[mask]['rmsd'], label='Qualified Seqs', color='green')
plt.scatter(df[~mask]['plddt'], df[~mask]['rmsd'], label='Unqualified Seqs', color='red', alpha=0.5)
plt.xlabel("plddt")
plt.ylabel("rmsd")
plt.legend()
plt.title("D: Design 0")
plt.savefig("D/Plots/D_Design_0.png")
plt.show()
