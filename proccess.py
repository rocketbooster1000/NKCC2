import os
import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot(design_identity: str, folders, plddt_threshold=0.7, rmsd_threshold=5, split_pdb="none", source="none"):
    if not os.path.exists(design_identity):
        print(f"Directory {design_identity} does not exist.")
        return

    if not os.path.exists(f"{design_identity}/Plots"):
        os.makedirs(f"{design_identity}/Plots")
        
    pd_files = []
    for folder in folders:
        for file in os.listdir(os.path.join(design_identity, folder)):
            if file.endswith(".csv"):
                pd_csv = pd.read_csv(os.path.join(design_identity, folder, file))
                if (split_pdb == "first"):
                    pd_csv = pd_csv.iloc[:pd_csv.shape[0] // 2]
                elif (split_pdb == "second"):
                    pd_csv = pd_csv.iloc[pd_csv.shape[0] // 2:]
                pd_files.append(pd_csv)

    df = pd.concat(pd_files, ignore_index=True)
    
    df.to_csv(f'{design_identity}/{design_identity}-master.csv', index=False)
    
    df_filtered = df[(df['plddt'] > plddt_threshold) & (df['rmsd'] < rmsd_threshold)]
    df_filtered.sort_values(by=['plddt', 'rmsd'], ascending=[False, True], inplace=True)

    df_filtered.to_csv(f"{design_identity}/{design_identity}-filtered.csv", index=False)



    plt.scatter(df_filtered['plddt'], df_filtered['rmsd'], label='Qualified Seqs', color='blue')
    plt.scatter(df[~df.index.isin(df_filtered.index)]['plddt'], df[~df.index.isin(df_filtered.index)]['rmsd'], label='Unqualified Seqs', color='red', alpha=0.5)
    plt.xlabel("plddt")
    plt.ylabel("rmsd")
    plt.legend()
    plt.title(f"Design {design_identity}")
    plt.savefig(f"{design_identity}/Plots/{design_identity}-Plot.png")
    
    
    plt.show()

# process_and_plot("D", ["temp0.3"])
# process_and_plot("E", ["temp0.3"], split_pdb="first", source="E F")