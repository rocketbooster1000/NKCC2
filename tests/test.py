import pandas as pd

pd_csv = pd.read_csv("D/temp0.3/0mpnn_results.csv")
pd_csv = pd_csv.iloc[:pd_csv.shape[0] // 2]
pd_csv.to_csv("D/temp0.3/0mpnn_results_first_half.csv", index=False)
